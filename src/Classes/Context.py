from EnumContextNames import ContextName
import QuestionBank


class Context:
    def __init__(self,*args):
        if len(args) == 1:
            self.context_name = args[0]
            self.question = QuestionBank.find(self.context_name)
        if len(args) == 2:
            self.context_name = args[0]
            self.question = [ContextName.EXITO, args[1]]
