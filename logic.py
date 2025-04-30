import csv
from voteing_gui import *

class Logic:
    def __init__(self, vote, voter_id):
        self.vote = vote
        self.voter_id = voter_id
    def id_verify(self):
        with open("vote.txt", "r") as file:
            for i in file.readlines():
                if i.strip() == self.voter_id:
                    Ui_MainWindow().label_4.setText(QtCore.QCoreApplication.translate(
                        "MainWindow",'<span style="color:red;">Already Voted</span>'))
                    return False
        self.add_vote()
        return True
    def add_vote(self):
        with open("vote.txt", "a") as file:
            writer = csv.writer(file)
            writer.writerow([self.voter_id, self.vote])
    def return_vote(self):
        with open("vote.txt", "r") as file:
            pass


