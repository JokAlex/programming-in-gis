import time
import qgis.core


class TwiceVeryActiveAlgorithm(qgis.core.QgsProcessingAlgorithm):
    def initAlgorithm(self, config=None):
        pass
        
    def processAlgorithm(self, parameters, context, feedback):
        for i in range(10):
            start = time.time()
            while time.time() < start + 0.25:
                pass
            feedback.setProgress(i * 10)
            
        feedback.setProcessedCount(1)
        
        for i in range(10):
            start = time.time()
            while time.time() < start + 0.25:
                pass
            feedback.setProgress(i * 10)
        return {}
    
    def name(self):
        return "very-active-algorithm"
    
    def displayName(self):
        return "Very active algorithm"
        
    def createInstance(self):
        return TwiceVeryActiveAlgorithm()

