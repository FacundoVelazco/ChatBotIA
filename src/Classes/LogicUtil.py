import aima3.utils
import aima3.logic
from Classes.Clausses import *
from Classes.EnumContextNames import ContextName
import aima3.logic
from aima3.logic import pl_resolution

class LogicUtil:
    def __init__(self):
        self.KB = aima3.logic.FolKB(getClausses())

    def tell(self,clausula:str):
        self.KB.tell((aima3.utils.expr(clausula)))
        return None
    def ask(self, clausula:str):
        resultado = self.KB.ask((aima3.utils.expr(clausula)))
        return resultado

    def askConditional(self, clausula: str):
        resultado = pl_resolution(self.KB,(aima3.utils.expr(clausula)))
        return resultado

    def claussesForContext(self,context_name : str):
        if context_name == ContextName.PRESENTACION.name:
            return presentationClausses()
        if context_name == ContextName.LOCACION.name:
            return locacionClausses()


