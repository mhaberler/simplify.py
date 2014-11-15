"""
simplify.py is a simple port of simplify.js by Vladimir Agafonkin
(https://github.com/mourner/simplify-js)

It uses a combination of Douglas-Peucker and Radial Distance algorithms.
"""

try:
    rangefunc = xrange
except NameError:
    rangefunc = range

def getSquareDistance2d(p1, p2):
    """
    Square distance between two points (x,y)
    """
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]

    return dx * dx + dy * dy


def getSquareDistance3d(p1, p2):
    """
    Square distance between two points (x,y,z)
    """
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]

    return dx * dx + dy * dy + dz * dz


def getSquareSegmentDistance2d(p, p1, p2):
    """
    Square distance between point and a segment
    """
    x = p1[0]
    y = p1[1]

    dx = p2[0] - x
    dy = p2[1] - y

    if dx or dy:
        t = ((p[0] - x) * dx + (p[1] - y) * dy) / (dx * dx + dy * dy)

        if t > 1:
            x = p2[0]
            y = p2[1]
        elif t > 0:
            x += dx * t
            y += dy * t

    dx = p[0] - x
    dy = p[1] - y

    return dx * dx + dy * dy


def getSquareSegmentDistance3d(p, p1, p2):
    """
    Square distance between point and a segment
    """
    x = p1[0]
    y = p1[1]
    z = p1[2]

    dx = p2[0] - x
    dy = p2[1] - y
    dz = p2[2] - z

    if dx or dy:
        t = ((p[0] - x) * dx + (p[1] - y) * dy + (p[2] - z) * dz) / \
            (dx * dx + dy * dy + dz * dz)

        if t > 1:
            x = p2[0]
            y = p2[1]
            z = p2[2]
        elif t > 0:
            x += dx * t
            y += dy * t
            z += dz * t

    dx = p[0] - x
    dy = p[1] - y
    dz = p[2] - z

    return dx * dx + dy * dy + dz * dz


def changemode(mode):
    """
    Change points to 2D/3D.
    """
    if mode == '2d':
        getSquareDistance = getSquareDistance2d
        getSquareSegmentDistance = getSquareSegmentDistance2d
    elif mode == '3d':
        getSquareDistance = getSquareDistance3d
        getSquareSegmentDistance = getSquareSegmentDistance3d
    else:
        # use your own functions
        pass


def simplifyRadialDistance(points, tolerance):

    prev_point = points[0]
    new_points = [prev_point]

    for point in points:

        if getSquareDistance(point, prev_point) > tolerance:
            new_points.append(point)
            prev_point = point

    if prev_point != point:
        new_points.append(point)

    return new_points


def simplifyDouglasPeucker(points, tolerance):

    first = 0
    last = len(points) - 1

    first_stack = []
    last_stack = []

    markers = [first, last]

    while last:
        max_sqdist = 0

        for i in rangefunc(first, last):
            sqdist = getSquareSegmentDistance(
                points[i], points[first], points[last])

            if sqdist > max_sqdist:
                index = i
                max_sqdist = sqdist

        if max_sqdist > tolerance:
            markers.append(index)

            first_stack.append(first)
            last_stack.append(index)

            first_stack.append(index)
            last_stack.append(last)

        # Can pop an empty array in Javascript, but not Python,
        # so check the list first
        first = first_stack.pop() if first_stack else None
        last = last_stack.pop() if last_stack else None

    markers.sort()

    return [points[i] for i in markers]


def simplify(points, tolerance=0.1, highestQuality=True):
    """
    Simplifies the points.

    `points`: A sequences of sequences of at least two numbers (int or float), the first
        two elements of each inner sequence are treated as coordinates. Extra elements
        (e.g. z coordinate, name, etc) of point sequences are ignored but preserved for
        points which remain.

    Examples
      * tuple of tuple - `((1,1), (2,3), (3,5), (5,5))`
      * tuple of array - `([1,1,'first'], [2,3,'second'], [5,8,'third'])`

    `tolerance (optional, 0.1 by default)`: Affects the amount of simplification that occurs (the smaller, the less simplification).

    `highestQuality (optional, True by default)`: Flag to exclude the distance pre-processing. Produces higher quality results, but runs slower.
    """
    sqtolerance = tolerance * tolerance

    if not highestQuality:
        points = simplifyRadialDistance(points, sqtolerance)

    points = simplifyDouglasPeucker(points, sqtolerance)

    return points

getSquareDistance = getSquareDistance2d
getSquareSegmentDistance = getSquareSegmentDistance2d

if __name__ == '__main__':
    import timeit
    points = ((1, 1), (2, 3), (3, 5), (5, 5))
    print(timeit.repeat(lambda: simplify(points)))
