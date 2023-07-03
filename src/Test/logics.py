from aima import logic
from aima import utils
from clauses import getClauses

def initKB():
    KB = logic.FolKB(getClauses())
    return KB

if __name__ == '__main__':
    KB = initKB()
    KB.ask(utils.expr('lenguaje(x)'))
