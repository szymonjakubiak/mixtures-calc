from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMenuBar, QMenu
from PyQt5.QtWidgets import QAction

from .DropDownMenu import DropDownMenu
from .InputBoxes import InputBoxes

class EpoxUi(QMainWindow):
    """GUI for EpoxyApp"""
    def __init__(self):
        """Initiates an instance of EpoxUi - GUI for 'Epoxy Calculator' app"""
        super().__init__()
        # Set main window's properties
        self.setWindowTitle('Mix Calculator')

        # Set the central widget
        self.generalMainLayout = QVBoxLayout() # main layout instance
        self.centralWidget = QWidget() # main widget instance
        self.centralWidget.setLayout(self.generalMainLayout)
        self.setCentralWidget(self.centralWidget)

        # Set top menu bar
        self.menubar = QMenuBar(self)
        self.menuData = QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        # Create actions
        self.actionReadData = QAction(self)
        self.actionWriteData = QAction(self)
        self.menuData.addAction(self.actionReadData)
        self.menuData.addAction(self.actionWriteData)
        self.menubar.addAction(self.menuData.menuAction())
        # Lable top menu
        self.labelTopMenuBar()

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

    def getReadWriteActions(self):
        """Return read and write QActions."""
        return (self.actionReadData, self.actionWriteData)

    def labelTopMenuBar(self):
        """Set visible labels for top menu bar."""
        self.menuData.setTitle("&Source file")
        self.actionReadData.setText("Read")
        self.actionWriteData.setText("Write")
