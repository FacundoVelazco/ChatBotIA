import aima3.utils
import aima3.logic
import Clausses

class LogicUtils:
    def __init__(self):
        self.KB = aima3.logic.FolKB(Clausses.getClausses())

