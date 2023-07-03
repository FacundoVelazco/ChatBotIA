import aima3.utils
import aima3.logic
import Clausses
from Classes.Sentence import Sentence


class LogicUtil:
    def __init__(self):
        self.KB = aima3.logic.FolKB(Clausses.getClausses())

    def tell(self,sentence:Sentence):
        return None
    def ask(self, sentence: Sentence):
        return None

