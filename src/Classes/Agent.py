from Sentence import Sentence
from LogicUtil import LogicUtil

class Agent:
    def __init__(self):
        self.raw_sentence = list()
        self.context = list()
        self.sentence = list()
        self.aima = LogicUtil()

    def addRawSentence(self, text: str):
        self.raw_sentence.append(text)

    def getAnswer(self):
        if len(self.raw_sentence) == 0:
            return ["Use addRawSentence first...", ""]

        last_raw_sentence = self.raw_sentence.pop()

        last_sentence = Sentence(last_raw_sentence)

        self.sentence.append(last_sentence)

        aima_result = self.consult(last_sentence)

        self.context.append()

    def consult(self,sentence : Sentence):

