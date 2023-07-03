import aima3.utils
import aima3.logic
from Classes.Clausses import getClausses
from Classes.Sentence import Sentence


class LogicUtil:
    def __init__(self):
        self.KB = aima3.logic.FolKB(getClausses())

    def tell(self,clausula:str):
        self.KB.tell((aima3.utils.expr(clausula)))
        return None
    def ask(self, clausula:str):
        resultado = self.KB.tell((aima3.utils.expr(clausula)))
        return resultado
