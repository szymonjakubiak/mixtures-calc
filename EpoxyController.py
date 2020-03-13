from EpoxyGUI import EpoxUi

class EpoxContrl():
    """EpoxyApp Controller Class"""
    def __init__(self, argView, argModel):
        self.view = argView
        self.model = argModel
        self.connectSignals()
    
    def connectSignals(self):
        """Connects specific signals to its slots by calling corresponding 'handle' method"""
        # Assing shorter names to QLineEdits
        wTotalMass = self.view.inputWidgetsDictionary['wTotalMass'][0]
        wResinMass = self.view.inputWidgetsDictionary['wResinMass'][0]
        wActivatorMass = self.view.inputWidgetsDictionary['wActivatorMass'][0]

        # Calling method on specific signal
        wTotalMass.textEdited.connect(self.handleTotalMass)
        wResinMass.textEdited.connect(self.handleResinMass)
        wActivatorMass.textEdited.connect(self.handleActivatorMass)

    def handleTotalMass(self):
        # Get current text
        currentText = self.view.inputWidgetsDictionary['wTotalMass'][0].text()
        # Calculating output for the other two QLineEdits
        outputList = self.model.calculateOnTotalMass(currentText)
        # Assigning new text to QLineEdits
        self.view.inputWidgetsDictionary['wResinMass'][0].setText(outputList[0])
        self.view.inputWidgetsDictionary['wActivatorMass'][0].setText(outputList[1])

    def handleResinMass(self):
        # Get current text
        currentText = self.view.inputWidgetsDictionary['wResinMass'][0].text()
        # Calculating output for the other two QLineEdits
        outputList = self.model.calculateOnResinMass(currentText)
        # Assigning new text to QLineEdits
        self.view.inputWidgetsDictionary['wTotalMass'][0].setText(outputList[0])
        self.view.inputWidgetsDictionary['wActivatorMass'][0].setText(outputList[1])
    
    def handleActivatorMass(self):
        # Get current text
        currentText = self.view.inputWidgetsDictionary['wActivatorMass'][0].text()
        # Calculating output for the other two QLineEdits
        outputList = self.model.calculateOnActivatorMass(currentText)
        # Assigning new text to QLineEdits
        self.view.inputWidgetsDictionary['wTotalMass'][0].setText(outputList[0])
        self.view.inputWidgetsDictionary['wResinMass'][0].setText(outputList[1])
