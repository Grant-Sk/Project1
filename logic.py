import csv
from voteing_gui import *
class Logic:

    def __init__(self, ui):
        """
        Initialize the Logic class with a UI object.
        finds out who they voted for.
        :param ui: - The UI object.
        """
        self.ui = ui
        self.vote = None
        self.ui.radioButton_2.toggled.connect(lambda checked: self.set_vote("Jane") if checked else None)
        self.ui.radioButton.toggled.connect(lambda checked: self.set_vote("Tommy") if checked else None)

    def set_vote(self, candidate):
        self.vote = candidate
    '''
    Sets the candidate they are voting for.
    :param: vote - The candidate vote.
    '''
    def id_verify(self):
        """
        Verifies the ID is in the correct format.
        displays messages accordingly.
        Sees if someone wants the current results.

        :param voter_id: The voters ID. is a 4 digit as a string.
        :param int_id: The voters ID. is a 4 digit as an integer.
        :return: None
        """
        voter_id = self.ui.lineEdit.text()
        if voter_id == "results":
            self.return_vote()
            return

        try:
            int_id = int(voter_id)
        except ValueError:
            self.ui.label_4.setText('<span style="color:red;">ID Must Be Digits Only</span>')
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
        """
        Adds the vote and voters ID to vote.csv file.
        :return: None
        """
        with open("vote.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([voter_id, self.vote])
        self.ui.radioButton.setAutoExclusive(False)
        self.ui.radioButton_2.setAutoExclusive(False)
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton.setAutoExclusive(True)
        self.ui.radioButton_2.setAutoExclusive(True)
        self.ui.label_4.setText(QtCore.QCoreApplication.translate("MainWindow", ""))
        self.ui.lineEdit.setText(QtCore.QCoreApplication.translate("MainWindow", ""))
    def return_vote(self):
        """
        Tallies the votes from the CSV file and displays the winner.
        :return: None
        """
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
            vote_total = Tommy
            win = "Tommy"
        elif Jane > Tommy:
            win = "Jane"
            vote_total = Jane
        else:
            win = "None"
            self.ui.label_4.setText(
            f'<span style="color:red;">No One Won The Election</span>')
            return
        if vote_total > 1:
            self.ui.label_4.setText(
                f'<span style="color:green;">{win} Won The Election With {vote_total} Votes!</span>')
        else:
            self.ui.label_4.setText(f'<span style="color:green;">{win} Won The Election With {vote_total} Vote!</span>')