from PyQt5.QtWidgets import QLineEdit, QGridLayout
from PyQt5.QtCore import QObjectCleanupHandler
from PyQt5.QtCore import Qt
from PyQt5.Qt import QIntValidator, QRegularExpressionValidator, QRegularExpression

class CompInputBoxes():
    """Handles a creation of text input area (ratios & components' names)"""
    def __init__(self):
        """CompInputBoxes default constructor"""
        # Layout for inputBoxes
        self.compInputLayout = QGridLayout()

        # QLineEdits for component's names
        self.compNameLineEdits = []
        # QLineEdits for ratios
        self.compRatioLineEdits = []

        # Building input region with a deafult value
        self.buildCompInputRegion()

    def buildCompInputRegion(self, numberOfComponenets = 2):
        """Builds input region based on number of componenets"""
        # Remove previous widgets from the inputRegion
        for nameEdit, ratioEdit in zip(self.compNameLineEdits, self.compRatioLineEdits):
            QObjectCleanupHandler().add(nameEdit)
            QObjectCleanupHandler().add(ratioEdit)
        # Empty the lists
        self.compNameLineEdits = []
        self.compRatioLineEdits = []

        # Creating new widgets' instances
        for index in range(numberOfComponenets):
            self.compNameLineEdits.append(QLineEdit())
            self.compRatioLineEdits.append(QLineEdit())

        # Setting text alignment for every QLineEdit
        for nameEdit, ratioEdit in zip(self.compNameLineEdits, self.compRatioLineEdits):
            nameEdit.setAlignment(Qt.AlignLeft)
            ratioEdit.setAlignment(Qt.AlignCenter)

        # Adding widgets to inputBoxes' layout
        for index, (nameEdit, ratioEdit) in enumerate(zip(self.compNameLineEdits, self.compRatioLineEdits)):
            self.compInputLayout.addWidget(nameEdit, index, 0)
            self.compInputLayout.addWidget(ratioEdit, index, 1)

        # Setting placeholder text for every QLineEdit and QValidators
        # Preparing validators
        ratioValidator = QIntValidator()
        nameValidator = QRegularExpressionValidator()
        nameValidator.setRegularExpression(QRegularExpression(r"[\w\d]*"))
        for index, (nameEdit, ratioEdit) in enumerate(zip(self.compNameLineEdits, self.compRatioLineEdits), start=1):
            strIndex = str(index)
            # Setting placeholders
            nameEdit.setPlaceholderText("Name " + strIndex)
            ratioEdit.setPlaceholderText("Ratio " + strIndex)
            # Setting validators
            nameEdit.setValidator(nameValidator)
            ratioEdit.setValidator(ratioValidator)

    def attachCompInputBoxes(self, generalLayout):
        """Adds compInputLayout to general layout of QDialog window"""
        generalLayout.addLayout(self.compInputLayout)


    def getAllLineEdits(self):
        """Rturns [[nameLineEdit,], [ratioLineEdit,]]"""
        return [self.compNameLineEdits, self.compRatioLineEdits]

    def getAllLineEditsData(self):
        """Returns a list [[ratios,], [names,]]"""
        ratiosList = []
        namesList = []

        # Getting text from every QLineEdit
        for ratioEdit, nameEdit in zip(self.compRatioLineEdits, self.compNameLineEdits):
            # Ratios
            ratiosList.append(int(ratioEdit.text()))
            # Names
            namesList.append(nameEdit.text())

        return [ratiosList, namesList]