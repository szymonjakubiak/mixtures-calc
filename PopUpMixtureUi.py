from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QSpinBox, QDialogButtonBox

from CompInputBoxes import CompInputBoxes

class PopUpMixtureUi (QDialog):
    """Class handling a constrution of the pop-up dialog window"""
    def __init__(self):
        """PopUpMixture constructor"""
        super().__init__()
        self.setWindowTitle('Adding a new mixture')

        # General layout for pop-up window
        self.generalComponentsLayout = QVBoxLayout()
        self.setLayout(self.generalComponentsLayout)

        # QLabel with basic info about QSpinBox
        self.componentsInfoLabel = QLabel('Number of components')
        # QSpinBox - number of components selection
        self.componentsNumberSelector = QSpinBox()
        # QDialogButtonBox - OK and Cancel buttons
        self.standardButtons = QDialogButtonBox()

        # text input area
        self.componentsInputBoxes = CompInputBoxes()

        # Building dialog buttons
        self.standardButtons.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        # Attach info label & QSpinBox to the general layout
        self.generalComponentsLayout.addWidget(self.componentsInfoLabel)
        self.generalComponentsLayout.addWidget(self.componentsNumberSelector)
        # Attach inputBoxes to the general layout
        self.componentsInputBoxes.attachCompInputBoxes(self.generalComponentsLayout)
        # Attach 'Cancel' and 'Ok' buttons
        self.generalComponentsLayout.addWidget(self.standardButtons)

        # Customize QSpinBox
        self.componentsNumberSelector.setMaximum(10)
        self.componentsNumberSelector.setMinimum(2)

    def getInputBoxes(self):
        """Returns the current instance of CompInputBoxes"""
        return self.componentsInputBoxes

    def getSpinBox(self):
        """Returns the current instance of QSpinBox"""
        return self.componentsNumberSelector

    def getStandardButtons(self):
        """Returns standard QDialog buttons - 'Cancel, 'Ok' (QDialogButtonBox)"""
        return self.standardButtons

    
