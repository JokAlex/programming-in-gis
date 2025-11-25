import qgis.core


class BestAlgorithm(qgis.core.QgsProcessingAlgorithm):
    def initAlgorithm(self, config=None):
        pass

    def processAlgorithm(self, parameters, context, feedback):
        return {}

    def name(self):
        return "best"

    def displayName(self):
        return "Best Algorithm Ever Made"

    def createInstance(self):
        return BestAlgorithm()
