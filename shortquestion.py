from subjective import *
class shortq(subjective):
    def __init__(self, file):
        super().__init__(file, 2)
    def __str__(self):
        return f'{super().__str__()}\n-----------------------------------\n----------------------------'
