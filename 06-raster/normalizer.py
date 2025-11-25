import qgis.core, qgis.utils
import math, numpy
from osgeo import gdal

def main():
    layer = qgis.utils.iface.activeLayer()
    uri = layer.source().replace("dem_reprojected", "raster")

    layer_dataset = gdal.Open(layer.source())
    layer_band = layer_dataset.GetRasterBand(1)

    driver = gdal.GetDriverByName("Gtiff")
    dataset = driver.Create(
        uri, 
        layer_dataset.RasterXSize, 
        layer_dataset.RasterYSize, 
        1, 
        gdal.GDT_Float32
    )

    min, max = layer_band.ComputeRasterMinMax()

    dataset.SetGeoTransform(layer_dataset.GetGeoTransform())
    dataset.SetProjection(layer_dataset.GetProjection())

    data = numpy.ma.masked_values(
        layer_band.ReadAsArray(), 
        layer_band.GetNoDataValue()
    )
    
    data = (data - min) / (max - min)
    data = data.filled(math.nan)
    dataset.GetRasterBand(1).WriteArray(data)

    dataset.GetRasterBand(1).SetNoDataValue(
        math.nan
    )
    dataset.FlushCache()

    new_layer = qgis.core.QgsRasterLayer(uri, "raster")
    qgis.core.QgsProject.instance().addMapLayer(new_layer)

main()
