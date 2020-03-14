import os.path

from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QLineEdit, QHBoxLayout, QVBoxLayout, QLabel
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

        # Create particular parts of the GUI
        self.buildDropDownList()
        self.buildInputRegion()
        
        # Check for default.dat file and create one if needed
        #   default.dat file contains an example list of mixtures
        self.checkDataFile('defaultTest.dat')

        # Load data from default file
        self.loadDataFromDefault(self.wMixturesList)

    def buildInputRegion(self):
        """Adds inputRegion to mainWindow's layout"""
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



"""
TODO:

"""