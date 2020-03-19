from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QComboBox

from DropDownMenu import DropDownMenu
from InputBoxes import InputBoxes

class EpoxUi(QMainWindow):
    """GUI for EpoxyApp"""
    def __init__(self):
        """Initiates an instance of EpoxUi - GUI for 'Epoxy Calculator' app"""
        super().__init__()
        # Set main window's properties
        self.setWindowTitle('Epoxy Calculator')

        # Set the central widget
        self.generalMainLayout = QVBoxLayout() # main layout instance
        self.centralWidget = QWidget() # main widget instance
        self.centralWidget.setLayout(self.generalMainLayout)
        self.setCentralWidget(self.centralWidget)

        # Creating particular parts of the GUI
        self.dropDownRegion = DropDownMenu()
        self.inputRegion = InputBoxes()

        # Attaching layouts to mainWindoLayout
        self.inputRegion.attachInputBoxes(self.generalMainLayout)
        self.dropDownRegion.attachDropDownMenu(self.generalMainLayout)
        

    def getDropDownMenu(self):
        """Returns the DropDownMenu class"""
        return self.dropDownRegion

    def getInputBoxes(self):
        """Returns the InputBoxes class"""
        return self.inputRegion
