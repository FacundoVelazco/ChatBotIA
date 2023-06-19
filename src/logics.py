from aima import logic
from aima import utils
from clauses import getClauses

def initKB():
    KB = logic.FolKB(getClauses())
    return KB