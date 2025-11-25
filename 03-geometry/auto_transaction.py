import qgis.core


layer = qgis.core.QgsMemoryProviderUtils.createMemoryLayer(
    "points",
    qgis.core.QgsFields(),
    qgis.core.QgsWkbTypes.Point,
    qgis.core.QgsCoordinateReferenceSystem("EPSG:4326"),
)

points = [(0, 0), (10, 0), (0, 10), (10, 10)]

with qgis.core.edit(layer):
    for x, y in points:
        feature = qgis.core.QgsFeature()
        feature.setGeometry(qgis.core.QgsPoint(x, y))
        layer.addFeature(feature)

qgis.core.QgsProject.instance().addMapLayer(layer)
print("Generated")
