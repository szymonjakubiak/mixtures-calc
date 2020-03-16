class EpoxMod():

    def __init__(self):
        """EpoxMod constructor"""
        self.wrongTypeMessage = 'NOT_A_NUMBER'
        self.resinRatiosList = []

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
<<<<<<< HEAD
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
=======
        
        [isValidNumber, outputList] = self.inputCheck(inputText)
        if not isValidNumber:
            return outputList
            
        # Assign input to inputString
        self.inputString = inputText
        # Input string to float conversion
        self.inputNumber = float(self.inputString)

        # Calculate resin mass
        self.resinMass = self.inputNumber / self.resinRatio
        self.resinMass = round(self.resinMass, self.digitNumber)
        # Calculate total mass
        self.totalMass = self.inputNumber + self.resinMass
        self.totalMass = round(self.totalMass, self.digitNumber)

        return [str(self.totalMass), str(self.resinMass)]

if __name__ == '__main__':
    """Testing the module"""
    emod = EpoxMod()

    # Setting resin ratio
    emod.setResinRatio(1/9)
    #emod.setResinRatio('a')
    #emod.setResinRatio(-3.0)

    # Calculate masses based on TotalMass
    emod_out = emod.calculateOnTotalMass('12.333330000a')
    print(emod_out)
    emod_out = emod.calculateOnTotalMass('10')
    print(emod_out)

    # Calculate masses based on ResinMass
    emod_out = emod.calculateOnResinMass('12.333330000a')
    print(emod_out)
    emod_out = emod.calculateOnResinMass('9.0')
    print(emod_out)

     # Calculate masses based on ActivatorMass
    emod_out = emod.calculateOnActivatorMass('12.333330000a')
    print(emod_out)
    emod_out = emod.calculateOnActivatorMass('1.0')
    print(emod_out)

    #Check input-checking method
    [bol, vals] = emod.inputCheck('12.1')
    print(bol)
    print(vals)
    [bol, vals] = emod.inputCheck('12.1a')
    print(bol)
    print(vals)
    [bol, vals] = emod.inputCheck('')
    print(bol)
    print(vals)
    
"""
TODO:
-Redefine model, instead of 3 separate functions add 1: solving system of linear equations (rectangular matrix [2x3], but 1 unknown is set a priori)
"""
>>>>>>> devDropDown
