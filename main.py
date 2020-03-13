import sys

from PyQt5.QtWidgets import QApplication
from EpoxyGUI import EpoxUi
from EpoxyController import EpoxContrl
from EpoxyModel import EpoxMod


def main():
    """Main function"""
    # Create an instance of QApplication
    application = QApplication(sys.argv)

    # Show the GUI
    viewGui = EpoxUi()
    viewGui.show()

    # Create instances of the model and the controller
    modelEpoxy = EpoxMod()
    guiController = EpoxContrl(argModel=modelEpoxy, argView=viewGui)

    # Setting resin ratio
    modelEpoxy.setResinRatio(1/9)

    # Execute app's main loop
    sys.exit(application.exec())

if __name__ == '__main__':
    main()