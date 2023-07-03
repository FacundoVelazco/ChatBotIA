from EnumContextNames import ContextName
import QuestionBank


class Context:
    def __init__(self, name: str):
        self.context_name = name.upper()
        self.question = QuestionBank.find(self.context_name)
