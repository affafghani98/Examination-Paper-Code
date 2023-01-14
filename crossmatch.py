from objective import *
from random import randint
class crossmatch(objective):
    def __init__(self, file, count = 1):
        super().__init__(file, count)
        self.count = count
        self.list1 = []
        self.list2 = []
        file.readline()
        for i in range(self.count):

            s = file.readline()
            self.list1.append(s)
            b = file.readline()
            self.list2.append(b)
    def __str__(self):
        string = question.__str__(self)+'\n'
        for i in range(len(self.list1)):
            index = randint(0,len(self.list1)-1)
            stmt1 = self.list1[index]
            self.list1.remove(stmt1)
            index = randint(0,len(self.list2)-1)
            stmt2 = self.list2[index]
            self.list2.remove(stmt2)
            string += stmt1 + '**  ' + stmt2 + '\n'
        return string + f'\nEnter Your Answers: '







# Write your code here :-)
