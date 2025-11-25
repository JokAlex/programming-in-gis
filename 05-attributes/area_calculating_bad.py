import PyQt5
import qgis.core, qgis.utils

source_layer = qgis.utils.iface.activeLayer()

fields = source_layer.fields()
if "area_proj" in fields:
    raise qgis.core.QgsProcessingException(
        "Attribute 'area_proj' already exists"
    )

fields.append(qgis.coreQgsField("area_proj", PyQt5.QtCore.QVariant.Double))

dest_layer = qgis.core.QgsMemoryProviderUtils.createMemoryLayer(
    "layer_with_area", fields, source_layer.wkbType(), source_layer.crs()
)

with qgis.core.edit(dest_layer):
    for feature in source_layer.getFeatures():
        feature.setFields(fields)
        feature["area_proj"] = feature.geometry().area()
        dest_layer.addFeature(feature)

qgis.core.QgsProject.instance().addMapLayer(dest_layer)
print("Generated")
