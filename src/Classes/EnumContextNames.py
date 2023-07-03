from enum import Enum


class ContextName(Enum):
    #TODO añadir mas contextos nombrados
    PRESENTACION = "PRESENTACION"
    LENGUAJE = "LENGUAJE"
    LOCACION = "LOCACION"

    def __str__(self):
        return f'{self.name}'
