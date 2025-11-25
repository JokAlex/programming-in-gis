import PyQt5
import qgis.core, qgis.utils

source_layer = qgis.utils.iface.activeLayer()

fields = source_layer.fields()
if "area_proj" in fields:
    raise qgis.core.QgsProcessingException(
        "Attribute 'area_proj' already exists"
    )

fields.append(QgsField("area_proj", PyQt5.QtCore.QVariant.Double))

dest_layer = qgis.core.QgsMemoryProviderUtils.createMemoryLayer(
    "layer_with_area",
    fields,
    source_layer.wkbType(),
    source_layer.crs()
)

with edit(dest_layer):
    for feature in source_layer.getFeatures():
        newFeature = qgis.core.QgsFeature(feature)
        newFeature.setFields(fields)
        for name, value in feature.attributeMap().items():
            newFeature[name] = value
        newFeature["area_proj"] = feature.geometry().area()
        dest_layer.addFeature(newFeature)

qgis.core.QgsProject.instance().addMapLayer(dest_layer)
print("generated")
