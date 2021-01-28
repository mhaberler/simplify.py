# simplify.py

simplify.py is a simple port of simplify.js by Vladimir Agafonkin
([https://github.com/mourner/simplify-js](https://github.com/mourner/simplify-js))

This branch is based on original work by @omarestrella and incorporates the
3d support code by @gumblex.

The code assumes no particular layout of the underlying data structure containing
point geometries, other than being an indexable sequence. Access to the actual
coordinates is delegated to a customizable accessor function which is an instantiation
parameter - simplify is now a class: Simplify2D or Simplify3D.

The simplifier can return either a list of integer markers of points to be retained in the
simplified polyline (returnMarkers=True), or a list of actual points (returnMarkers=False).


## Usage

```python
import simplify
s = simplify.Simplify2D([accessor=AccessorFunction])
s = simplify.Simplify3D([accessor=AccessorFunction])
r = s.simplify(points,
	      [,tolerance=tolerance],
	      [,highestQuality=highestQuality]
	      [,returnMarkers=True|False]
	      [,kwargs])

```

`points`: A sequences of sequences of at least two numbers.

`AccessorFunction`: a callable which - given a sequence of objects and an
integer index value, returns a sequence of 2 (2D case) or 3 coordinates (3D case)
of the object. Any extraneous values are ignored.

Any extra kwargs to simplify() are passed to the accessor function.

`tolerance (optional, 0.1 by default)`: Affects the amount of simplification that occurs (the smaller, the less simplification).

`highestQuality (optional, True by default)`: Flag to exclude the distance pre-processing. Produces higher quality results, but runs slower.

`returnMarkers (optional, False by default)`: return a list of marker indices instead of actual elements of the
underlying structure. Useful to skip a superfluous list creation step in case just markers are needed.


## Examples:

Simplifying a GeoJSON FeatureCollection of Point features with a custom
accessor function (see [https://github.com/mhaberler/simplify.py/blob/master/example.py](example.py)):

```python
from simplify import Simplify3D
import geojson

def featureAccessor(sequence, index, **kwargs):
    return sequence[index].geometry.coordinates

s = Simplify3D(accessor=featureAccessor)

# contains a FeatureCollection of Points
fn = "radiosonde.geojson"
with open(fn, 'r') as file:
    str = file.read()
    j = geojson.loads(str.encode("utf8"))

highestQuality = False
tolerance = 0.01

print(s.simplify(j.features,
                 tolerance=tolerance,
                 highestQuality=highestQuality,
                 returnMarkers=False))
```


These sequences can be handled with the default accessor function (2D case):
  * list of lists  - `[[1,1], [2,3], [3,5], [5,5]]`
  * list of tuple  - `[(1,1), (2,3), (3,5), (5,5)]`
  * tuple of tuple - `((1,1), (2,3), (3,5), (5,5))`
  * tuple of lists - `([1,1], [2,3], [5,8])`


## Notes

This might not be the most Pythonic of codes, but works for me. I'm happy to entertain patches and improvements.
