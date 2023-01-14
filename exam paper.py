from question import *
from objective import *
from mcq import *
from fillintheblanks import *
from crossmatch import *
from subjective import *
from shortQ import *
from longq import *
class exam:
    def __init__(self, title):
        self.title = title
        self.mcq =[]
        self.fillintheblank = []
        self.crossmatch = []
        self.short = []
        self.long = []
        a = int(input("Enter count of MCQ questions (1-6)"))
        b = int(input("Enter count of fill in the blanks count questions (1-6)"))
        c = int(input("Enter count of statements in crosshatch question(1-6)"))
        d = int(input("Enter count of short questions"))
        e = int(input("Enter count of long questions"))
        file1 = open("mcq.txt", 'r')
        file2 = open("fill_in_the_blanks.txt", 'r')
        file3 = open("crossmatch.txt", "r")
        file4 = open("short.txt", "r")
        file5 = open("long.txt", "r")
        for i in range(a):
            a = mcq(file1)
            self.mcq.append(a)
        for j in range(b):
            a = fillintheblanks(file2)
            self.fillintheblank.append(a)
        for k in range(c):
            a = crossmatch(file3)
            self.crossmatch.append(a)
        for l in range(d):
            a = shortq(file4)
            self.short.append(a)
        for m in range(e):
            a = longq(file5)
            self.long.append(a)

    def __str__(self):
            a = '\n'
            for i in self.mcq:
                a += i.__str__()
            for i in self.fillintheblank:
                a+= i.__str__()
            for i in self.crossmatch:
                a +=i.__str__()
            for i in self.short:
                a += i.__str__()
            for i in self.long:
                a += i.__str__()
            return a
def main():
    c = exam('maths')
    print(c)
main()


























# Write your code here :-)
