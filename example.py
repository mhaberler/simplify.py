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
