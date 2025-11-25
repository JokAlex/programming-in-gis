import qgis.core


# Searchs for layers with name "Base layer"
found_layers = qgis.core.QgsProject.instance().mapLayersByName("Base layer")
if len(found_layers) > 0:
    print(found_layers)
else:
    print('No layers with the name "Base layer" were found.')
