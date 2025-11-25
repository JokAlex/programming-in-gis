import qgis.core


layer1 = qgis.core.QgsProject.instance().mapLayersByName("layer1")[0]
layer2 = qgis.core.QgsProject.instance().mapLayersByName("layer2")[0]

source_crs = layer1.crs()
dest_crs = layer2.crs()

transform_context = qgis.core.QgsProject.instance().transformContext()
transform = qgis.core.QgsCoordinateTransform(source_crs, dest_crs, transform_context)

for feature in layer1.getFeatures():
    geometry = feature.geometry()
    print(geometry)
    geometry.transform(transform)
    print(geometry)
    print("---")
