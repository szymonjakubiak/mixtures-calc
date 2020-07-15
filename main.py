import sys
from PyQt5.QtWidgets import QApplication

from EpoxyGUI import EpoxUi
from EpoxyController import EpoxContrl
from EpoxyModel import EpoxMod
from PopUpMixtureUi import PopUpMixtureUi


def main():
    """Main function"""
    # Create an instance of QApplication, EpoxUi, PopUpMixtureUi
    application = QApplication(sys.argv)
    viewGui = EpoxUi()
    dialogGui = PopUpMixtureUi()
    # Create instances of the model and the controller
    modelEpoxy = EpoxMod()
    guiController = EpoxContrl(argModel=modelEpoxy, argView=viewGui, argDialog=dialogGui)
    guiController.loadDefaultData()
    # Execute app's main loop
    sys.exit(application.exec())

if __name__ == '__main__':
    main()