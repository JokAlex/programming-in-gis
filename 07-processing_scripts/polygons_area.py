import qgis.core
import PyQt5


class PolygonsArea(qgis.core.QgsProcessingAlgorithm):
    INPUT_LAYER = 'INPUT_LAYER'
    OUTPUT_LAYER = 'OUTPUT_LAYER'
    
    def initAlgorithm(self, config=None):
        self.addParameter(
            qgis.core.QgsProcessingParameterFeatureSource(
                self.INPUT_LAYER,
                'Polygons',
                [qgis.core.QgsWkbTypes.Polygon]
            )
        )
        
        self.addParameter(
            qgis.core.QgsProcessingParameterFeatureSink(
                self.OUTPUT_LAYER,
                'Polygons with area'
            )
        )
        
    def processAlgorithm(self, parameters, context, feedback):
        source_layer = self.parameterAsSource(parameters, self.INPUT_LAYER, context)
            
        fields = source_layer.fields()
        if "area" in fields.names():
            raise qgis.core.QgsProcessingException(
                "Attribute 'area' already exists"
            )

        fields.append(qgis.core.QgsField("area", PyQt5.QtCore.QVariant.Double))
        
        output, output_layer_name = self.parameterAsSink(
            parameters,
            self.OUTPUT_LAYER, 
            context, 
            fields,
            source_layer.wkbType(),
            source_layer.sourceCrs()
        )
                
        calc = qgis.core.QgsDistanceArea()
        calc.setEllipsoid('WGS84')

        transform_context = qgis.core.QgsProject.instance().transformContext()
        calc.setSourceCrs(source_layer.sourceCrs(), transform_context)
        
        progress_step = 100 / source_layer.featureCount()
            
        for i, feature in enumerate(source_layer.getFeatures()):
            newFeature = qgis.core.QgsFeature(feature)
            newFeature.setFields(fields)
            for name, value in feature.attributeMap().items():
                newFeature[name] = value
            newFeature["area"] = calc.measureArea(feature.geometry())
            output.addFeature(newFeature)
        
            feedback.setProgress(i * progress_step)
            
        return {self.OUTPUT_LAYER: output}
    
    def name(self):
        return "polygons-area"
    
    def displayName(self):
        return "Area of polygons"
        
    def createInstance(self):
        return PolygonsArea()

