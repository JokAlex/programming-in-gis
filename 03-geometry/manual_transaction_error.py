import qgis.core


layer = qgis.core.QgsMemoryProviderUtils.createMemoryLayer(
    "points",
    qgis.core.QgsFields(),
    qgis.core.QgsWkbTypes.Point,
    qgis.core.QgsCoordinateReferenceSystem("EPSG:4326")
)

points = [(0, 0), (10, 0), (0, 10), (10, 10)]

layer.startEditing()  # starting a transaction

for x, y in points:
    feature = qgis.core.QgsFeature()
    feature.setGeometry(qgis.core.QgsPoint(x, y))
    layer.addFeature(feature)

# Adding a feature with another type of geometry
wrong_feature = qgis.core.QgsFeature()
wrong_feature.setGeometry(
    qgis.core.QgsLineString([
        qgis.core.QgsPoint(0, 0),
        qgis.core.QgsPoint(10, 10)
    ])
)
layer.addFeature(wrong_feature)

layer.commitChanges()  # commiting a transaction

qgis.core.QgsProject.instance().addMapLayer(layer)
print("generated")  # oops...
