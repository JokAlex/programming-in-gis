import random
import PyQt5
import qgis.core


fields = qgis.core.QgsFields()
fields.append(qgis.core.QgsField("my_id", PyQt5.QtCore.QVariant.Int))
fields.append(qgis.core.QgsField("random_int", PyQt5.QtCore.QVariant.Int))
fields.append(qgis.core.QgsField("random_real", PyQt5.QtCore.QVariant.Double))

layer = qgis.core.QgsMemoryProviderUtils.createMemoryLayer(
    "layer_without_geometry", fields
)

with qgis.core.edit(layer):
    for i in range(5):
        feature = qgis.core.QgsFeature(fields)
        feature["my_id"] = i
        feature["random_int"] = random.randint(-100, 100)
        feature["random_real"] = random.random()
        layer.addFeature(feature)

qgis.core.QgsProject.instance().addMapLayer(layer)
print("Generated")
