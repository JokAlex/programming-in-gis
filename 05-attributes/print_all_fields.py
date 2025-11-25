import qgis.utils

layer = qgis.utils.iface.activeLayer()
for field in layer.fields():
    print(field)
    
print(layer.fields()["int_value"])
