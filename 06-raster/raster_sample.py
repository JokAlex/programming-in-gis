import qgis.core, qgis.utils

layer = qgis.utils.iface.activeLayer()
provider = layer.dataProvider()

print(provider.sample(qgis.core.QgsPointXY(734596, 6402083), 1))
print(provider.sample(qgis.core.QgsPointXY(782419, 6373195), 1))
