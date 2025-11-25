import qgis.core


def crs_units_are_meters(crs):
    if qgis.core.Qgis.QGIS_VERSION_INT < 33000:
        return crs.mapUnits() == \
            qgis.core.QgsUnitTypes.DistanceUnit.DistanceMeters
    else:
        return crs.mapUnits() == qgis.core.Qgis.DistanceUnit.Meters


print(crs_units_are_meters(qgis.core.QgsCoordinateReferenceSystem("EPSG:3857")))
