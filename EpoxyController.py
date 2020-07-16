from functools import partial
from PyQt5.QtWidgets import QFileDialog

from FileOperator import FileOperator

class EpoxContrl():
    """EpoxyApp Controller Class"""
    def __init__(self, argView, argModel, argDialog):
        self.view = argView
        self.model = argModel
        self.dialog = argDialog
        
        # Handles operations on files
        self.fileOperator = FileOperator()

        # Connect signals
        self.connectLineEditsSignals()
        self.connectDropDownSelection()
        self.connectAddRemoveButtons()
        self.connectSpinBoxSelector()
        self.connectCancelOk()
        self.connectTopMenuBar()

        # Show gui
        self.view.show()
    
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

    def connectAddRemoveButtons(self):
        """Connects 'Add' and 'Remove' buttons' signals"""
        # Get buttons from DropDownMenu
        dropDownMenu = self.view.getDropDownMenu()
        addButton = dropDownMenu.getAddButton()
        removeButton = dropDownMenu.getRemoveButton()

        # Connect 'Add' button so it executes Pop-up window
        addButton.clicked.connect(self.dialog.exec)

        # Connect 'Remove' button
        removeButton.clicked.connect(self.handleRemoveMixture)

    def connectSpinBoxSelector(self):
        """Connects SpinBox selection, so that it builds a new CompInputBoxes"""
        # Get SpinBox from PopUpMixtureUi
        spinBox = self.dialog.getSpinBox()

        # Connect the signal to handler method
        spinBox.valueChanged.connect(partial(self.handleSpinBoxChanged, spinBox))

    def connectCancelOk(self):
        """Dialog signals: accepted() ('Ok' pressed) and rejected() ('Cancel' pressed)"""
        # Connect 'Ok'
        self.dialog.accepted.connect(self.handleDialogOk)
        # Connect 'Cancel'
        self.dialog.rejected.connect(self.handleDialogCancel)

    def connectTopMenuBar(self):
        """Connects top menu bar and its actions to proper slots."""
        actionRead, actionWrite = self.view.getReadWriteActions()
        actionRead.triggered.connect(self.handleReadAction)
        actionWrite.triggered.connect(self.handleWriteAction)

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
        # Get current text from QComboBox
        currentText = qComboBox.currentText()

        # Set the model with a new data
        self.model.setModelData(currentText)

        # Get new set of labels & size
        newLabels = self.model.getLabels()
        newInputWidgetsNumber = self.model.getModelSize()

        # Build inputRegion based on a new data
        inputRegion = self.view.getInputBoxes()
        # Set new number of inputBoxes
        inputRegion.buildInputRegion(newInputWidgetsNumber-1)
        # Set new Labels
        inputRegion.setAllLabels(newLabels)

        #IMPORTANT recreate connections for newly build widgets
        self.connectLineEditsSignals()

    def handleSpinBoxChanged(self, spinBox):
        """Handles creation of a new set of QLineEdits for mixtures data, after the QSpinBox changes its value"""
        # Get a new number of components (in SpinBox)
        newNumber = spinBox.value()

        # Build CompInputBoxes based on the new number
        inputBoxes = self.dialog.getInputBoxes()
        inputBoxes.buildCompInputRegion(newNumber)

    def handleDialogCancel(self):
        """Closes pop-up window and performs cleaning"""
        self.cleanDialogBox()

    def handleDialogOk(self):
        """Load user input into a model and clean pop-up window"""
        # Check if input not empty
        if not self.dialog.getInputBoxes().isAnyInputEmpty():
            # Get input data entered by a user
            inputData = self.dialog.getInputBoxes().getAllLineEditsData()
            # Encode the input
            encoder = self.model.getEncoder()
            dataString = encoder.encodeData(inputData[0], inputData[1])
            # Add encoded data to the end of the drop-down menu
            dropDownMenu = self.view.getDropDownMenu()
            comboBox = dropDownMenu.getQComboBox()
            comboBox.addItem(dataString)
        # Cleaning
        self.cleanDialogBox()

    def handleRemoveMixture(self):
        """Removes current mixture from drop-down menu."""
        # Get drop down menu (QComboBox)
        dropDown = self.view.getDropDownMenu().getQComboBox()
        # Delete item at current index
        dropDown.removeItem(dropDown.currentIndex())

    def cleanDialogBox(self):
        """Returns pop-up window to its default shape"""
        # Rebuild CompInputBoxes to its default shape
        inputBoxes = self.dialog.getInputBoxes()
        inputBoxes.buildCompInputRegion()
        # Change spin box number to default=2
        spinBox = self.dialog.getSpinBox()
        spinBox.setValue(2)

    def handleReadAction(self):
        """Load mixtures from file to drop-down menu (QComboBox)."""
        # Reading data from file
        fileName, _ = QFileDialog.getOpenFileName(self.view, "Select source file", "", "Mixtures data (*.dat);;All Files (*)")
        mixtures = self.fileOperator.readFromFile(fileName)
        # Appending data to QComboBox
        self.view.getDropDownMenu().appendItems(mixtures)

    def handleWriteAction(self):
        """Write all items(strings) from drop-down menu (QComboBox) to given file."""
        # Getting data-strings from QComboBox
        comboBox = self.view.getDropDownMenu().getQComboBox()
        dataStrings = [comboBox.itemText(index) for index in range(comboBox.count())]
        # Writing data to selected file
        fileName, _ = QFileDialog.getSaveFileName(self.view, "Select save location", "", "Mixtures data (*.dat);;All Files (*)")
        if fileName[-4:] != ".dat": # maintain '.dat' convention for new files
            fileName += ".dat"
        self.fileOperator.saveToFile(dataStrings, fileName)