import qgis.core
import qgis.utils


layer = qgis.utils.iface.activeLayer()

with qgis.core.edit(layer):
    for feature in layer.getFeatures():
        # Coping of geometry
        geometry = feature.geometry()
        for id, vertex in enumerate(geometry.vertices()):
            geometry.moveVertex(
                qgis.core.QgsPoint(vertex.x() + 10, vertex.y() + 10),
                id
            )
        # Re-assigning of geometry
        feature.setGeometry(geometry)
        # Updating feature to apply changes to layer (because feature is COW)
        layer.updateFeature(feature)

print("done")
