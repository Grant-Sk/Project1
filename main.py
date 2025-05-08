from voteing_gui import *
import sys
def main():
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