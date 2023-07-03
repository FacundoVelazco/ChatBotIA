from EnumContextNames import ContextName
import QuestionBank

class Context:
    def __init__(self, name: str):
        self.context_name = name.upper()
        self.question = None

    #definir como va a seleccionar una pregunta, quizaen base a la info faltante
    def getQuestion(self):
        QuestionBank.find()
