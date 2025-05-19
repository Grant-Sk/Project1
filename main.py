from voteing_gui import *
import sys
def main():
    """
    Method to start the application.
    opens and resets the vote.csv file.
    :return: None
    """
    with open('vote.csv', 'w', newline='') as csvfile:
        pass
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setFixedSize(650, 600)
    MainWindow.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()
    