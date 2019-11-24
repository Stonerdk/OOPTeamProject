from openpyxl import load_workbook
from abc import *

class Dictionary:
    @abstractmethod
    def Similarity(self):
        pass

class Sim_print:
    @abstractmethod
    def Result_print(self):
        pass
