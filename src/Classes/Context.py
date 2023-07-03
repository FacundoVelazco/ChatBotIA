from Classes.EnumContextNames import ContextName
import Classes.QuestionBank as Qb


class Context:
    def __init__(self,*args):
        if len(args) == 1:
            self.context_name = args[0]
            self.question = Qb.find(self.context_name)
        if len(args) == 2:
            self.context_name = args[0]
            self.question = [ContextName.EXITO, args[1]]
