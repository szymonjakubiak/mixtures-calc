from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton, QComboBox

class DropDownMenu():
    """Class configuring drop-down list and it's features"""
    def __init__(self):
        """DropDownMenu constructor"""
        # General layout for drop-down area
        self.dropGeneralLayout = QGridLayout()

        # Builds features for drop-down menu
        self.buildDropDownMenu()

    def buildDropDownMenu(self):
        """Builds features for drop-down menu"""
        # Main drop-down feature
        self.dropQComboBox = QComboBox()
        # Drop-down add entry button
        self.dropAddButton = QPushButton()
        #Drop-down remove entry button
        self.dropRemoveButton = QPushButton()

        # Adding QWidgets to dropGeneralLayout
        self.dropGeneralLayout.addWidget(self.dropRemoveButton, 0, 0) # 1x1
        self.dropGeneralLayout.addWidget(self.dropQComboBox, 0, 1, 1, 2) # 1x3
        self.dropGeneralLayout.addWidget(self.dropAddButton, 0, 3) # 1x1

        # Setting text for the buttons
        self.dropAddButton.setText('Add')
        self.dropRemoveButton.setText('Remove')

    def attachDropDownMenu(self, mainWindowLayout):
        """Attaches dropGeneralLayout to the layout of the main window"""
        mainWindowLayout.addLayout(self.dropGeneralLayout)

    def getQComboBox(self):
        """Returns the QComboBox storing drop-down list"""
        return self.dropQComboBox

    def getAddButton(self):
        """Returns the AddButton"""
        return self.dropAddButton

    def getRemoveButton(self):
        """Returns the RemoveButton"""
        return self.dropRemoveButton

    def addOneItem(self, text):
        """Adds an item to the drop-down list"""
        self.dropQComboBox.addItem(text)

    def setAllItems(self, textList):
        """Sets all entries to the drop-down list"""
        # Clear all previous entries
        self.dropQComboBox.clear()
        # Add new entries
        self.dropQComboBox.addItems(textList)