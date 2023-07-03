from enum import Enum


class ContextName(Enum):
    #TODO añadir mas contextos nombrados
    PRESENTACION = "PRESENTACION"
    LENGUAJE = "LENGUAJE"
    LOCACION = "LOCACION"
    EXITO = "EXITO"
    IDIOMA = "IDIOMA"
    MODALIDAD = "MODALIDAD"
    DISPONIBILIDAD = "DISPONIBILIDAD"
    EQUIPO = "EQUIPO"
    ARQUITECTURA = "ARQUITECTURA"
    SUELDO = "SUELDO"
    CEO = "CEO"
    def __str__(self):
        return f'{self.name}'
