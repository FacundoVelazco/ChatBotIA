import aima3.utils
import aima3.logic
from Classes.Clausses import getClausses
from Classes.Sentence import Sentence


class LogicUtil:
    def __init__(self):
        self.KB = aima3.logic.FolKB(getClausses())

    def tell(self,sentence:Sentence):
        return None
    def ask(self, sentence: Sentence):
        return None

