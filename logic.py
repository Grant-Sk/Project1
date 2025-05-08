import csv
from voteing_gui import *
class Logic:
    def __init__(self, ui):
        self.ui = ui
        self.vote = None
        self.ui.radioButton_2.toggled.connect(lambda checked: self.set_vote("Jane") if checked else None)
        self.ui.radioButton.toggled.connect(lambda checked: self.set_vote("Tommy") if checked else None)

    def set_vote(self, candidate):
        self.vote = candidate

    def id_verify(self):
        voter_id = self.ui.lineEdit.text()

        if voter_id == "close vote":
            self.return_vote()
            return

        try:
            int_id = int(voter_id)
        except ValueError:
            self.ui.label_4.setText('<span style="color:red;">ID Must Be Numbers</span>')
            return

        if not (1000 <= int_id <= 9999):
            self.ui.label_4.setText('<span style="color:red;">ID Must Be 4 Digits</span>')
            return

        with open("vote.csv", "r") as file:
            for line in file:
                if voter_id in line.strip():
                    self.ui.label_4.setText('<span style="color:red;">Already Voted</span>')
                    return

        if self.vote is None:
            self.ui.label_4.setText('<span style="color:red;">No candidate selected</span>')
            return

        self.add_vote(voter_id)
        self.ui.label_4.setText(f'<span style="color:green;">Vote Submitted for {self.vote}</span>')

    def add_vote(self, voter_id):
        with open("vote.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([voter_id, self.vote])
        self.ui.label_4.setText(QtCore.QCoreApplication.translate("MainWindow", ""))
        self.ui.lineEdit.setText(QtCore.QCoreApplication.translate("MainWindow", ""))
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton.setChecked(False)
    def return_vote(self):
        Tommy = 0
        Jane = 0

        with open("vote.csv", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) < 2:
                    continue
                _, vote = parts
                if vote == "Tommy":
                    Tommy += 1
                elif vote == "Jane":
                    Jane += 1

        if Tommy > Jane:
            win = "Tommy"
        elif Jane > Tommy:
            win = "Jane"
        else:
            win = "None"
        print(win)
        self.ui.MainWindow.close()
        self.result_window = QtWidgets.QMainWindow()
        self.result_ui = win_menu()
        self.result_ui.setupUi(self.result_window)
        self.result_ui.label.setText(f"{win} WON!")
        self.result_window.setFixedSize(200, 200)
        self.result_window.show()
