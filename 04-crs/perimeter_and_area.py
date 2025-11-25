import qgis.core
import qgis.utils


layer = qgis.utils.iface.activeLayer()
print(layer.crs())

calc = qgis.core.QgsDistanceArea()
calc.setEllipsoid('WGS84')

transform_context = qgis.core.QgsProject.instance().transformContext()
calc.setSourceCrs(layer.crs(), transform_context)

for feature in layer.getFeatures():
    geometry = feature.geometry()

    perimeter = calc.measurePerimeter(geometry)
    area = calc.measureArea(geometry)
    print(f"perimeter, area = {perimeter:8.2f}, {area:12.2f}")
