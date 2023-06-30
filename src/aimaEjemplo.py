# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Import libraries
import aima3.utils
import aima3.logic


# The main entry point for this module
def main():
    # Create an array to hold clauses
    clauses = []
    # Add first-order logic clauses (rules and fact)
    clauses.append(aima3.utils.expr("(American(x) & Weapon(y) & Sells(x, y, z) & Hostile(z)) ==> Criminal(x)"))
    clauses.append(aima3.utils.expr("Enemy(Nono, America)"))
    clauses.append(aima3.utils.expr("Owns(Nono, M1)"))
    clauses.append(aima3.utils.expr("Missile(M1)"))
    clauses.append(aima3.utils.expr("(Missile(x) & Owns(Nono, x)) ==> Sells(West, x, Nono)"))
    clauses.append(aima3.utils.expr("American(West)"))
    clauses.append(aima3.utils.expr("Missile(x) ==> Weapon(x)"))
    # Create a first-order logic knowledge base (KB) with clauses
    KB = aima3.logic.FolKB(clauses)
    # Add rules and facts with tell
    KB.tell(aima3.utils.expr('Enemy(Coco, America)'))
    KB.tell(aima3.utils.expr('Enemy(Jojo, America)'))
    KB.tell(aima3.utils.expr("Enemy(x, America) ==> Hostile(x)"))
    # Get information from the knowledge base with ask
    hostile = KB.ask(aima3.utils.expr('Hostile(x)'))
    criminal = KB.ask(aima3.utils.expr('Criminal(x)'))
    consulta = KB.ask(aima3.utils.expr('American(West)'))

    # Print answers
    #print('Hostile?')
    #print(hostile)
    #print('\nCriminal?')
    #print(criminal)
    print(consulta)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
