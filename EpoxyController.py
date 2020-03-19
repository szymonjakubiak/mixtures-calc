from functools import partial

from FileOperator import FileOperator

class EpoxContrl():
    """EpoxyApp Controller Class"""
    def __init__(self, argView, argModel):
        self.view = argView
        self.model = argModel
        
        # Handles operations on files
        self.fileOperator = FileOperator()

        # Connect signals
        self.connectLineEditsSignals()
        self.connectDropDownSelection()
    
    def loadDefaultData(self):
        """Loads default data into model & updates GUI"""
        # Get a string list from the default file
        stringList = self.fileOperator.readFromFile()

        # Set a content for dropDownMenu
        dropDown = self.view.getDropDownMenu()
        dropDown.setAllItems(stringList)

    def connectLineEditsSignals(self):
        """Connects specific signals to its slots"""
        # Get an instance of inputRegion
        inputRegion = self.view.getInputBoxes()
        # Load a list of QLineEdits
        allLineEdits = inputRegion.getAllLineEdits()
        # Connect every 'textEdit' signal to handleTextEditOnIndex function with widgetIndex as an argument
        for index, lineEdit in enumerate(allLineEdits):
            lineEdit.textEdited.connect(partial(self.handleTextEditOnIndex, lineEdit, index, len(allLineEdits)))

    def connectDropDownSelection(self):
        """Connects dropDown selection signal to its slot"""
        # Get an instance of QComboBox from DropDownMenu
        dropDown = self.view.getDropDownMenu()
        comboBox = dropDown.getQComboBox()

        # Delegate signal to a specific method
        comboBox.currentIndexChanged.connect(partial(self.handleComboIndexChange, comboBox))

    def handleTextEditOnIndex(self, lineEdit, widgetIndex, numberOfWidgets):
        """When specific lineEdit is triggered, generate and set output for other widgets"""
        # Getting text from the triggered lineEdit
        currentText = lineEdit.text()
        # Calculating output for all lineEdits
        outputList = self.model.calculateOnIndex(currentText, widgetIndex, numberOfWidgets)
        # Setting calculated output
        inputRegion = self.view.getInputBoxes()
        inputRegion.setAllLineEditsText(outputList)

    def handleComboIndexChange(self, qComboBox):
        """Handles an event when combo box changes its index"""
        pass