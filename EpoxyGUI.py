import os.path

from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox

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
        ### INPUT REGION ####
        self.buildInputRegion()
         # Adding inputGeneralLayout to general layout for mainWindow
        self.generalMainLayout.addLayout(self.inputGeneralLayout)

        ### DROP DOWN LIST ###
        self.buildDropDownList()

        
        # Check for default.dat file and create one if needed
        #   default.dat file contains an example list of mixtures
        self.checkDataFile('defaultTest.dat')

        # Load data from default file
        self.loadDataFromDefault(self.wMixturesList)

    def buildInputRegion(self, numberOfComponents=2):
        """Builds inputRegion for a given number of Mixture's components"""
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

    def getAllLineEdits(self):
        """Returns a list containing all QLineEdits"""
        return self.inputQLineEdits

    def setAllLineEditsText(self, textList):
        """Set text in all line edits based on input textList"""
        # Check if lists' lengths are equal
        if len(textList) == len(self.inputQLineEdits):
            # Assign text to every QLineEdit
            for qLineEdit, text in zip(self.inputQLineEdits, textList):
                qLineEdit.setText(text)
        # If input textList has incorrect length
        else:
            print("Cannot set text for QLineEdits. List's length does not match")

    def buildDropDownList(self):
        """Adds dropDownList to mainWindow's layout"""
        # Create an instance of drop-down list for listing all available mixtures
        self.wMixturesList = QComboBox()

        # Adding the widget do general layout for mainWindow
        self.generalMainLayout.addWidget(self.wMixturesList)
        

    def loadDataFromDefault(self, wComboBox):
        """Loads data from the default file 'data.dat' to wComboBox"""
        with open("data.dat") as defaulData:
            for line in defaulData:
                # Clear a line not to add empty line to every entry in drop-down list
                clearString = line.strip('\n')
                wComboBox.addItem(clearString)

    def checkDataFile(self, fileName):
        if not os.path.isfile(fileName):
            with open(fileName, 'w') as writeFile:
                defaultMixture1 = "{:<30}".format('DP500 + Epoxy220') + '1 : 10' + '\n'
                defaultMixture2 = "{:<30}".format('DP30000 + EpoxXXy220') + '3 : 7' + '\n'
                writeFile.write(defaultMixture1)
                writeFile.write(defaultMixture2)

