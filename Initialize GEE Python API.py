import ee
import geemap
ee.Authenticate()
ee.Initialize(project="my-project-332613")
sent1=ee.ImageCollection("COPERNICUS/S1_GRD").filterDate("2018-01-01","2019-01-01").filter(ee.Filter.eq('instrumentMode','IW')).filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')).first()

point = ee.Geometry.Point([50.836977185981276,32.702907801743585])


sample = sent1.sample(region=point, scale=10)


sample_data = sample.getInfo()

print(sample_data)


vis_params = {
    'bands': ['VV'],
    'min': -1,
    'max': 1,

}


Map = geemap.Map()
Map.addLayer(sent1, {'min': -1, 'max': 1}, 'sent1')
Map.centerObject(point, 10)
Map.add_layer(sent1, vis_params, 'VV')

Map.add_marker(location=point.coordinates().getInfo())
Map



