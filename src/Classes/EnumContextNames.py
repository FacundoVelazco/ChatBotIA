from enum import Enum


class ContextName(Enum):
    PRESENTACION = "PRESENTACION"
    MODALIDAD = "MODALIDAD"
    LOCACION = "LOCACION"
    DISPONIBILIDAD = "DISPONIBILIDAD"
    LENGUAJE = "LENGUAJE"
    EQUIPO = "EQUIPO"
    IDIOMA = "IDIOMA"
    ARQUITECTURA = "ARQUITECTURA"
    SUELDO = "SUELDO"
    CEO = "CEO"
    EXITO = "EXITO"
    FINAL = "FINAL"

    def __str__(self):
        return f'{self.name}'
