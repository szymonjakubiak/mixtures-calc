class EpoxMod():
    def checkInput(self, inputText):
        """Checks if input is a valid number and returns Bool"""
        for letter in inputText:
            if letter not in list('0123456789.'):
                return False
        return True

    def setResinRatio(self, inputResinRatio):
        """Setting ResinRatio = activatorMass / resinMass"""
        assert type(inputResinRatio) == type(1.0), 'ResinRatio must be of a float type'
        assert inputResinRatio > 0.0, 'ResinRatio cannot be negative'
        self.resinRatio = inputResinRatio

    def calculateOnTotalMass(self, inputText):
        """
        User set TotalMass

        output = [resinMass, activatorMass]
        """
        # Check if input is a float string
        if not self.checkInput(inputText):
            return ['INPUT_NOT_A_NUMBER', 'INPUT_NOT_A_NUMBER']
        # Check if input is not an empty string
        if inputText == '':
            return ['', '']
        
        # Assign input to inputString
        self.inputString = inputText
        # Check number of digits in input
        self.digitNumber = len(inputText)
        # Input string to float conversion
        self.inputNumber = float(self.inputString)

        # Calculate resin mass
        self.resinMass = self.inputNumber / (1 + self.resinRatio)
        self.resinMass = round(self.resinMass, self.digitNumber)
        # Calculate activator mass
        self.activatorMass = self.inputNumber - self.resinMass
        self.activatorMass = round(self.activatorMass, self.digitNumber)

        return [str(self.resinMass), str(self.activatorMass)]


    def calculateOnResinMass(self, inputText):
        """
        User set ResinMass

        output = [totalMass, activatorMass]
        """
        
        # Check if input is a float string
        if not self.checkInput(inputText):
            return ['INPUT_NOT_A_NUMBER', 'INPUT_NOT_A_NUMBER']
        # Check if input is not an empty string
        if inputText == '':
            return ['', '']
            
        # Assign input to inputString
        self.inputString = inputText
        # Input string to float conversion
        self.inputNumber = float(self.inputString)

        # Calculate activator mass
        self.activatorMass = self.resinRatio * self.inputNumber
        self.activatorMass = round(self.activatorMass, self.digitNumber)
        # Calculate total mass
        self.totalMass = self.activatorMass + self.inputNumber
        self.totalMass = round(self.totalMass, self.digitNumber)

        return [str(self.totalMass), str(self.activatorMass)]

    def calculateOnActivatorMass(self, inputText):
        """
        User set ActivatorMass

        output = [totalMass, resinMass]
        """
        
        # Check if input is a float string
        if not self.checkInput(inputText):
            return ['INPUT_NOT_A_NUMBER', 'INPUT_NOT_A_NUMBER']
        # Check if input is not an empty string
        if inputText == '':
            return ['', '']
            
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
    
"""
TODO:
-Add check case for empty string ''
-Move repeating checks out of EpoxMod class / implement separeted method
"""