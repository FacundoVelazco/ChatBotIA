from Classes.Agent import Agent
from Classes.EnumContextNames import ContextName


class Manager:
    def __init__(self):
        self.agent = Agent()

    def start(self):
        mensajesBienvenida()
        while True:
            contexto_previo = self.agent.context.__getitem__(len(self.agent.context) - 1)
            print(contexto_previo.question[1])
            if (contexto_previo.context_name == ContextName.EXITO.name) or (contexto_previo.context_name == ContextName.FINAL.name):
                user_input = "x"
            else:
                user_input = input("-- ")

            if user_input == "x":
                print("¡¡Adios!!")
                break

            self.agent.addRawSentence(user_input)

            answer = self.agent.getAnswer()


def mensajesBienvenida():
    print("------------------------------------")
    print("Bienvenido al agente virtual de RRHH")
    print("  ")
    print("Lo guiaré en la ardua tarea de encontrar una posición de trabajo dentro del sector IT")
    print("------------------------------------")
    print("¿Como se encuentra el dia de hoy?")
    print("Ingrese x para salir...")
