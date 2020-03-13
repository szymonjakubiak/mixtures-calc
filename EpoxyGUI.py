from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QLineEdit, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class EpoxUi(QMainWindow):
    """GUI for EpoxyApp"""
    def __init__(self):
        super().__init__()
        # Set main window's properties
        self.setWindowTitle('Epoxy Calculator')

        # Set the central widget
        self.generalMainLayout = QVBoxLayout() # main layout instance
        self.centralWidget = QWidget() # main widget instance
        self.centralWidget.setLayout(self.generalMainLayout)
        self.setCentralWidget(self.centralWidget)

        # Create particular parts of the GUI
        self.buildInputRegion()
        #self.buildDropDownList()
        
        # Load data from default file
        #self.loadDataFromDefault()

    def buildInputRegion(self):
        # Creating dictionary with QWidgets for input area
        self.inputWidgetsDictionary = {}

        # Creating QLineEdit and QLabel for every input box
        self.inputWidgetsDictionary['wTotalMass'] = [QLineEdit(), QLabel()]
        self.inputWidgetsDictionary['wResinMass'] = [QLineEdit(), QLabel()]
        self.inputWidgetsDictionary['wActivatorMass'] = [QLineEdit(), QLabel()]
        #...[0] - QLineEdit
        #...[1] - QLabel

        # Setting text for input labels
        self.inputWidgetsDictionary['wTotalMass'][1].setText('Total mass')
        self.inputWidgetsDictionary['wResinMass'][1].setText('Resin mass')
        self.inputWidgetsDictionary['wActivatorMass'][1].setText('Activator mass')

        # General layout for input area
        self.inputGeneralLayout = QHBoxLayout()

        # Loop over every input 'box'
        for inputWidgetName in self.inputWidgetsDictionary:
            # Setting text allignment for every line edit
            self.inputWidgetsDictionary[inputWidgetName][0].setAlignment(Qt.AlignLeft)

            # Add QVBoxLayout for every 'lineEdit-label' pair
            pair = QVBoxLayout()
            pair.addWidget(self.inputWidgetsDictionary[inputWidgetName][0])
            pair.addWidget(self.inputWidgetsDictionary[inputWidgetName][1])
            self.inputWidgetsDictionary[inputWidgetName].append(pair)
            #...[2] - QVBoxLayout

            # Adding every pairLayout to input area layout
            self.inputGeneralLayout.addLayout(pair)

        # Adding inputGeneralLayout to general layout for mainWindow
        self.generalMainLayout.addLayout(self.inputGeneralLayout)
        