from objective import  *
class fillintheblanks(objective):
    def __init__(self,file, marks = 1):
        super().__init__(file, marks)
    def __str__(self):
        return f' {super().__str__()}\nEnter your answer:\n\n'


