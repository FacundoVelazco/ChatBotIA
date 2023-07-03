from Agent import Agent


class Manager:
    def __init__(self):
        self.agent = Agent()

    def start(self):
        mensajesBienvenida()
        while True:
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