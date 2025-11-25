import qgis.core, qgis.utils
import math, numpy
from osgeo import gdal

def calc_brightness(dn, l_min, l_max, q_cal_min, q_cal_max):
    return (l_max - l_min) / (q_cal_max - q_cal_min) * (dn - q_cal_min) + l_min

def main():
    layer = qgis.utils.iface.activeLayer()
    uri = layer.source().replace("blue1", "energy_brightness")

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

    dataset.SetGeoTransform(layer_dataset.GetGeoTransform())
    dataset.SetProjection(layer_dataset.GetProjection())

    data = numpy.ma.masked_values(
        layer_band.ReadAsArray(), 
        layer_band.GetNoDataValue()
    ).astype(numpy.float32)
    
    RADIANCE_MAXIMUM_BAND_2 = 784.65924
    RADIANCE_MINIMUM_BAND_2 = -64.79742
    
    QUANTIZE_CAL_MAX_BAND_2 = 65535
    QUANTIZE_CAL_MIN_BAND_2 = 1
    
    vectorized_calc = numpy.vectorize(calc_brightness)
    result = vectorized_calc(
        data, 
        RADIANCE_MINIMUM_BAND_2, 
        RADIANCE_MAXIMUM_BAND_2,
        QUANTIZE_CAL_MIN_BAND_2,
        QUANTIZE_CAL_MAX_BAND_2
    )
    dataset.GetRasterBand(1).WriteArray(result.filled(math.nan))

    dataset.GetRasterBand(1).SetNoDataValue(
        math.nan
    )
    dataset.FlushCache()

    new_layer = qgis.core.QgsRasterLayer(uri, "energy brightness")
    qgis.core.QgsProject.instance().addMapLayer(new_layer)

main()
