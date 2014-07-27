### simplify.py

simplify.py is a simple port of simplify.js by Vladimir Agafonkin ([https://github.com/mourner/simplify-js](https://github.com/mourner/simplify-js))

### Usage

```
import simplify
simplify(points, tolerance, highQuality)
```

`points`: A sequence (e.g. tuple or array) of dictionaries, containing x, y coordinates: `{'x': int/float, 'y': int/float}`
	or a sequence of sequences of at least two numbers (int or float), the first 
	two elements of each inner sequence are treated as coordinates. Extra elements (e.g. z 
	coordinate, name, etc) of both point sequences and dicts are ignored but preserved for 
	points which remain. 

Examples
  * array of dict - `[{'x': 1, 'y': 1}, {'x': 2, 'y': 3}, {'x': 3, 'y': 5} ]`
  * tuple of tuple - `((1,1), (2,3), (3,5), (5,5))`
  * tuple of array - `([1,1,'first'], [2,3,'second'], [5,8,'third'])`
 
`tolerance (optional, 0.1 by default)`: Affects the amount of simplification that occurs (the smaller, the less simplification).

`highestQuality (optional, True by default)`: Flag to exclude the distance pre-processing. Produces higher quality results, but runs slower.