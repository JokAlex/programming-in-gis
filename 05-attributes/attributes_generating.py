import random
import PyQt5
import qgis.core


fields = QgsFields()
fields.append(QgsField("my_id", PyQt5.QtCore.QVariant.Int))
fields.append(QgsField("random_int", PyQt5.QtCore.QVariant.Int))
fields.append(QgsField("random_real", PyQt5.QtCore.QVariant.Double))

layer = qgis.core.QgsMemoryProviderUtils.createMemoryLayer(
    "layer_without_geometry",
    fields
)

with edit(layer):
    for i in range(5):
        feature = QgsFeature(fields)
        feature["my_id"] = i
        feature["random_int"] = random.randint(-100, 100)
        feature["random_real"] = random.random()
        layer.addFeature(feature)

qgis.core.QgsProject.instance().addMapLayer(layer)
print("generated")
