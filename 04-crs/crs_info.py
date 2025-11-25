import qgis.core


def print_crs_info(crs):
    if crs.isValid():
        print("CRS", crs.authid(), "is valid")
        print("Map units:", crs.mapUnits())
    else:
        print("CRS is invalid")
    print("-----")

print_crs_info(qgis.core.QgsCoordinateReferenceSystem("EPSG:4326"))
print_crs_info(qgis.core.QgsCoordinateReferenceSystem("EPSG:3857"))

print_crs_info(
    qgis.core.QgsCoordinateReferenceSystem(
        "PROJ:+proj=lcc +lat_0=-37 +lon_0=145 +lat_1=-36 +lat_2=-38 "
        "+x_0=2500000 +y_0=2500000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 "
        "+units=m +no_defs"
    )
)

print_crs_info(qgis.core.QgsCoordinateReferenceSystem("EPSG:2"))
