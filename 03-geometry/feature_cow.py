import qgis.core, qgis.utils

layer = qgis.utils.iface.activeLayer()

with qgis.core.edit(layer):
    feature = layer.getFeature(1)
    geometry = feature.geometry()
    for id, vertex in enumerate(geometry.vertices()):
        geometry.moveVertex(
            qgis.core.QgsPoint(vertex.x() + 10, vertex.y() + 10), id
        )
    feature.setGeometry(geometry)
    feature.setId(3)
    layer.updateFeature(feature)

print("Done")
