from functools import partial

class EpoxContrl():
    """EpoxyApp Controller Class"""
    def __init__(self, argView, argModel):
        self.view = argView
        self.model = argModel
        self.connectSignals()
    
    def connectSignals(self):
        """Connects specific signals to its slots"""

        # Load a list of QLineEdits
        allLineEdits = self.view.getAllLineEdits()
        # Connect every 'textEdit' signal to handleTextEditOnIndex function with widgetIndex as an argument
        for index, lineEdit in enumerate(allLineEdits):
            lineEdit.textEdited.connect(partial(self.handleTextEditOnIndex, lineEdit, index, len(allLineEdits)))

    def handleTextEditOnIndex(self, lineEdit, widgetIndex, numberOfWidgets):
        """When specific lineEdit is triggered, generate and set output for other widgets"""
        # Getting text from the triggered lineEdit
        currentText = lineEdit.text()
        # Calculating output for all lineEdits
        outputList = self.model.calculateOnIndex(currentText, widgetIndex, numberOfWidgets)
        # Setting calculated output
        self.view.setAllLineEditsText(outputList)
