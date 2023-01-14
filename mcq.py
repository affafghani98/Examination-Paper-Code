from objective import *
class mcq(objective):
    def __init__(self, file, marks = 1):
        super().__init__(file, marks)

        self.choice1 = file.readline()
        self.choice2 = file.readline()
        self.choice3 = file.readline()
        self.choice4 = file.readline()
    def __str__(self):

        return  f"{super().__str__()}'\n' {self.choice1}'\n'{self.choice2}'\n'{self.choice3}'\n'{self.choice4}'\n 'enter your choice:**\n"

