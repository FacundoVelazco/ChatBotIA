#  Copyright (c) 2023.
#  el copicopi

# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Import libraries
import aima3.utils
import aima3.logic
from aima3.logic import pl_resolution


# The main entry point for this module
def main():
    # Create an array to hold clauses
    clauses = []
    # Add first-order logic clauses (rules and fact)

    clauses.append(aima3.utils.expr("Nombre(Bruno)"))
    clauses.append(aima3.utils.expr("Nombre(Bruno) ==> Puesto(Ceo)"))

    clauses.append(aima3.utils.expr("Lenguaje(x) ==> LengUser(x)"))
    clauses.append(aima3.utils.expr("Lenguaje(Java)"))
    # Create a first-order logic knowledge base (KB) with clauses
    KB = aima3.logic.FolKB(clauses)
    # Add rules and facts with tell

    # Get information from the knowledge base with ask
    consulta = aima3.utils.expr("Lenguaje(Java)")


    print(pl_resolution(KB, consulta))
    valor_string : dict = KB.ask(consulta)
    print(valor_string.values())
    for v in valor_string.values():
        print(v.__str__()," ",type(v.__str__()))

    print("KB.ask= ", KB.ask(consulta))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
