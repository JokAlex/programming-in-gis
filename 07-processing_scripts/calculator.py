import qgis.core


class Calculator(qgis.core.QgsProcessingAlgorithm):
    LHS = "LHS"
    RHS = "RHS"
    OPERATOR = "OPERATOR"
    OPERATORS = ["+", "-", "*", "/"]

    def initAlgorithm(self, config=None):
        self.addParameter(
            qgis.core.QgsProcessingParameterNumber(
                self.LHS,
                "Number 1",
                type=qgis.core.QgsProcessingParameterNumber.Double,
            )
        )

        self.addParameter(
            qgis.core.QgsProcessingParameterNumber(
                self.RHS,
                "Number 2",
                type=qgis.core.QgsProcessingParameterNumber.Double,
            )
        )

        self.addParameter(
            qgis.core.QgsProcessingParameterEnum(
                self.OPERATOR, "Operator", self.OPERATORS
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        lhs = self.parameterAsDouble(parameters, self.LHS, context)
        rhs = self.parameterAsDouble(parameters, self.RHS, context)
        operatorId = self.parameterAsEnum(parameters, self.OPERATOR, context)
        result = 0

        if self.OPERATORS[operatorId] == "+":
            result = lhs + rhs
        elif self.OPERATORS[operatorId] == "-":
            result = lhs - rhs
        elif self.OPERATORS[operatorId] == "*":
            result = lhs * rhs
        elif self.OPERATORS[operatorId] == "/":
            if rhs == 0:
                feedback.reportError("Division by zero")
                return {}
            result = lhs / rhs

        feedback.pushInfo(
            f"{lhs} {self.OPERATORS[operatorId]} {rhs} = {result}"
        )
        return {}

    def name(self):
        return "calculator"

    def displayName(self):
        return "Simple Calculator"

    def createInstance(self):
        return Calculator()
