### simplify.py

simplify.py is a simple port of simplify.js by Vladimir Agafonkin
([https://github.com/mourner/simplify-js](https://github.com/mourner/simplify-js))

This fork speeds up the code. Because of the huge overhead in Python's dict, and
few codes use dicts for points, I dropped the dict support.

### Usage

```python
import simplify
simplify.simplify(points, tolerance, highQuality)
```

`points`: A sequences of sequences of at least two numbers (int or float), the first
	two elements of each inner sequence are treated as coordinates. Extra elements
	(e.g. z coordinate, name, etc) of point sequences are ignored but preserved for
	points which remain.

Examples
  * tuple of tuple - `((1,1), (2,3), (3,5), (5,5))`
  * tuple of array - `([1,1,'first'], [2,3,'second'], [5,8,'third'])`

`tolerance (optional, 0.1 by default)`: Affects the amount of simplification that occurs (the smaller, the less simplification).

`highestQuality (optional, True by default)`: Flag to exclude the distance pre-processing. Produces higher quality results, but runs slower.

### 3D points

Change the alias for 2D points: `simplify.changemode('2d')`
Change the alias for 3D points: `simplify.changemode('3d')`
