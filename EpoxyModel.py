from MixturesEncoderDecoder import MixturesEncoderDecoder

class EpoxMod():

    def __init__(self):
        """EpoxMod constructor"""
        # Message when user inputs wrong text != valid float
        self.wrongTypeMessage = 'NOT_A_NUMBER'

        # Handles string <-> data coding
        self.mixturesCoder = MixturesEncoderDecoder()

        """
        stringList = self.fileOperator.readFromFile()
        [self.resinRatiosList, self.labelsList] = self.mixturesCoder.decodeString(stringList)
        """

        # List for storing recently decoded labels
        self.labelsList = []
        # List for storing mixtue's ratio recently in use
        self.resinRatiosList = []

    def setModelData(self, inputString):
        """Loads to model a particular mixture"""
        # Decode a string to usable data
        [self.resinRatiosList, self.labelsList] = self.mixturesCoder.decodeString(inputString)

    def getModelSize(self):
        """Return a number of input boxes"""
        return len(self.resinRatiosList)

    def getLabels(self):
        """Returns a list of recently decoded labels"""
        return self.labelsList

    def setResinRatios(self, inputResinRatios):
        """
        Setting ResinRatio, for example mixture 1:9
        inputResinRatios = [1, 9] -> resinRatiosList = [10, 1, 9]
        """
        self.resinRatiosList = []
        # First element == total mass
        self.resinRatiosList.append(0)
        for number in inputResinRatios:
            # Calculating total mass
            self.resinRatiosList[0] = self.resinRatiosList[0] + number
            # Appending componenets' 'fractions'
            self.resinRatiosList.append(number)

    def calculateOnIndex(self, inputText, widgetIndex, numberOfWidgets):
        """
        Returns a list of strings for every QLineEdit
        inputText - text send by triggered QLineEdit
        widgetIndex - index of triggered QLineEdit
        """
        # Check for empty string
        if inputText == '':
            return numberOfWidgets * ['']

        # Check if input is a valid number
        try:
            inputFloat = float(inputText)
        # Returns error message, does not change the input QLineEdit
        except ValueError:
            msg = numberOfWidgets * [self.wrongTypeMessage]
            msg[widgetIndex] = inputText
            return msg

        # Coefficient for computing other fields
        rho = inputFloat / self.resinRatiosList[widgetIndex]
        # Input length for unified rounding of output
        stringLength = len(inputText)

        # Loop over every mixture's component and calculate output value
        outputFloats = []
        for originalRatio in self.resinRatiosList:
            floatValue = rho * originalRatio
            floatValue = round(floatValue, stringLength)
            # Appending to a list
            outputFloats.append(floatValue)

        # Convert every float to string
        outputStrings = numberOfWidgets * ['']
        for index in range(len(outputFloats)):
            # Float -> String conversion
            if not index == widgetIndex:
                outputStrings[index] = str(outputFloats[index])
            # Do not change the text for trigged QLineEdit
            else:
                outputStrings[index] = inputText

        return outputStrings
