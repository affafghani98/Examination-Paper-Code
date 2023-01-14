from abc import *
class question(ABC):
    qno = 1
    def __init__(self, file, marks = 1):


        self.description = file.readline()
        self.marks = marks
        question.qno += 1
    @abstractmethod
    def __str__(self):
        return f'question no. {question.qno}\tmarks : {self.marks}\n description:{self.description} '
















        f
# Write your code here :-)
