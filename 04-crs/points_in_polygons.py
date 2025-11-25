import qgis.core


points = qgis.core.QgsProject.instance().mapLayersByName("points")[0]
polygons = qgis.core.QgsProject.instance().mapLayersByName("polygons")[0]

if points.crs() != polygons.crs():
    raise qgis.core.QgsProcessingException("Layers must have the same CRS")

result = qgis.core.QgsMemoryProviderUtils.createMemoryLayer(
    "points in polygons",
    qgis.core.QgsFields(),
    qgis.core.QgsWkbTypes.Point,
    points.crs()
)

with qgis.core.edit(result):
    for polygon in polygons.getFeatures():
        polygon_geometry = polygon.geometry()
        engine = qgis.core.QgsGeometry.createGeometryEngine(
            polygon_geometry.constGet()
        )
        for point in points.getFeatures():
            point_geometry = point.geometry()
            if engine.contains(point_geometry.constGet()):
                result_point = qgis.core.QgsFeature()
                result_point.setGeometry(point_geometry)
                result.addFeature(result_point)

qgis.core.QgsProject.instance().addMapLayer(result)
