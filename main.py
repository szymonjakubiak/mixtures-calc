import sys
from PyQt5.QtWidgets import QApplication

from lib import EpoxyGUI, EpoxyController, EpoxyModel, PopUpMixtureUi

def main():
    """Main function"""
    # Create an instance of QApplication, EpoxUi, PopUpMixtureUi
    application = QApplication(sys.argv)
    viewGui = EpoxyGUI.EpoxUi()
    dialogGui = PopUpMixtureUi.PopUpMixtureUi()
    # Create instances of the model and the controller
    modelEpoxy = EpoxyModel.EpoxMod()
    guiController = EpoxyController.EpoxContrl(argModel=modelEpoxy, argView=viewGui, argDialog=dialogGui)
    guiController.loadDefaultData()
    # Execute app's main loop
    sys.exit(application.exec())

if __name__ == '__main__':
    main()