import qgis.utils


layer = qgis.utils.iface.activeLayer()
print(layer.crs())
for feature in layer.getFeatures():
    geometry = feature.geometry()
    print(f"perimeter, area = {geometry.length():8.2f}, {geometry.area():12.2f}")
