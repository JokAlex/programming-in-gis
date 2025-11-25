import qgis.core, qgis.processing


class ThresholdAlgorithm(qgis.core.QgsProcessingAlgorithm):
    SOURCE_RASTER = 'SOURCE_RASTER'
    SOURCE_BAND = 'SOURCE_BAND'
    THRESHOLD = 'THRESHOLD'
    OUTPUT = 'OUTPUT'


    def initAlgorithm(self, config=None):
        self.addParameter(
            qgis.core.QgsProcessingParameterRasterLayer(
                self.SOURCE_RASTER, 'Source raster'
            )
        )
        
        self.addParameter(
            qgis.core.QgsProcessingParameterBand(
                self.SOURCE_BAND, 'Source band', 1, self.SOURCE_RASTER
            )
        )
        
        self.addParameter(
            qgis.core.QgsProcessingParameterNumber(
                self.THRESHOLD, 
                'Threshold', 
                type=qgis.core.QgsProcessingParameterNumber.Double
            )
        )
        
        self.addParameter(
            qgis.core.QgsProcessingParameterRasterDestination(
                self.OUTPUT, 'Binary mask layer'
            )
        )


    def processAlgorithm(self, parameters, context, feedback):
        source_layer = self.parameterAsRasterLayer(
            parameters, 
            self.SOURCE_RASTER, 
            context
        )
        
        source_band = self.parameterAsInt(parameters, self.SOURCE_BAND, context)
        
        threshold = self.parameterAsDouble(parameters, self.THRESHOLD, context)
        
        output_path = self.parameterAsOutputLayer(
            parameters, 
            self.OUTPUT, 
            context
        )
          
        source_band_str = f'"{source_layer.name()}@{source_band}"'
        formula = f'{source_band_str} > {threshold}'
 
        qgis.processing.run(
            "qgis:rastercalculator",
            {
                'LAYERS': [source_layer],
                'EXPRESSION': formula,
                'OUTPUT': output_path,
            },
            feedback=feedback,
            context=context,
            is_child_algorithm=True
        )

        return {self.OUTPUT: output_path}


    def name(self):
        return 'threshold'


    def displayName(self):
        return 'Threshold'


    def createInstance(self):
        return ThresholdAlgorithm()
        