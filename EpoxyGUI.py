from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout
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

        # Creating particular parts of the GUI
        ### INPUT REGION ####
        self.buildInputRegion()
         # Adding inputGeneralLayout to general layout for mainWindow
        self.generalMainLayout.addLayout(self.inputGeneralLayout)

        ### DROP DOWN LIST ###
        #self.buildDropDownList()
        
        # Load data from default file
        #self.loadDataFromDefault()

    def buildInputRegion(self, numberOfComponents=2):
        # Creating lists with QWidgets for input area
        self.inputQLineEdits = []
        self.inputQLabelList = []

        # Creating QLineEdit and QLabel for every input box,  =numberOfComponents + 1
        for componentIndex in range(numberOfComponents+1):
           # +1, TotalMass's window included
           self.inputQLineEdits.append(QLineEdit())
           self.inputQLabelList.append(QLabel())

        # Setting text for input labels
        self.inputQLabelList[0].setText('Total Mass') # First label
        for number, qLabel in enumerate(self.inputQLabelList[1:], start=1): # Other labels
            qLabel.setText('Component {} Mass'.format(number))

        # Setting text allignment for every line edit
        for qLineEdit in self.inputQLineEdits:
            qLineEdit.setAlignment(Qt.AlignLeft)

        # General layout for input area
        self.inputGeneralLayout = QGridLayout()

        # Setting layout for input area
        for columnNumber in range(numberOfComponents+1):
            # Assigning shorter names
            qLineEdit = self.inputQLineEdits[columnNumber]
            qLabel = self.inputQLabelList[columnNumber]

            self.inputGeneralLayout.addWidget(qLineEdit, 0, columnNumber)
            self.inputGeneralLayout.addWidget(qLabel, 1, columnNumber)
