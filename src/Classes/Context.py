import QuestionBank

class Context:
    def __init__(self, name: str):
        self.name = name
        self.question = None

    #definir como va a seleccionar una pregunta, quizaen base a la info faltante
    def getQuestion(self):
