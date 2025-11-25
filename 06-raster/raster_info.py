import qgis.core, qgis.utils

layer = qgis.utils.iface.activeLayer()

if not isinstance(layer, qgis.core.QgsRasterLayer):
    raise qgis.core.QgsProcessingException("Expected raster layer")

print("extent =", layer.extent())
print("crs =", layer.crs())
print("width, height =", layer.width(), layer.height())
print("spatial resolution x =", layer.rasterUnitsPerPixelX())
print("spatial resolution y =", layer.rasterUnitsPerPixelY())
