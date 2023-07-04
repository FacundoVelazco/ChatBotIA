from aima3 import utils
from Classes.LogicUtil import LogicUtil


def normalizer(text: str):
    text = text.replace(' ', '_')
    return text.capitalize()


def successCheck(aima: LogicUtil):
    puestos = list()
    if aima.KB.ask(utils.expr("Puesto(Frontend)")):
        puestos.append("FrontEnd Developer")
    if aima.KB.ask(utils.expr("Puesto(Backend)")):
        puestos.append("BackEnd Developer")
    if aima.KB.ask(utils.expr("Puesto(Fullstack)")):
        puestos.append("FullStack Developer")
    if aima.KB.ask(utils.expr("Puesto(TeamLeader)")):
        puestos.append("Team Leader")
    if aima.KB.ask(utils.expr("Puesto(Softwareengineermanager)")):
        puestos.append("Software Engineer Manager")
    if aima.KB.ask(utils.expr("Puesto(Cto)")):
        puestos.append("Chief Technology Officer")

    return puestos
