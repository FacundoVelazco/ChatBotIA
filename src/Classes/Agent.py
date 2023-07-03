from Classes.Sentence import Sentence
from Classes.LogicUtil import LogicUtil
from Classes.Context import Context
from Classes.EnumContextNames import ContextName
import spacy


class Agent:
    def __init__(self):
        self.raw_sentence = list()
        self.context = list()
        self.sentence = list()
        self.aima = LogicUtil()
        init_context = Context(ContextName.PRESENTACION.name)
        self.context.append(init_context)

    def addRawSentence(self, text: str):
        self.raw_sentence.append(text)

    def getAnswer(self):
        if len(self.raw_sentence) == 0:
            return ["Use addRawSentence first...", ""]

        # Cadena ingresada por el usuario
        last_raw_sentence = self.raw_sentence.__getitem__(len(self.raw_sentence) - 1)
        # Cadenas procesada por spacy
        last_sentences = self.defSentences(last_raw_sentence)
        # Voy a usar solo la primera #TODO arreglar algun dia
        self.sentence.append(last_sentences[0])
        # Creamos un contexto nuevo y lo devolvemos.
        new_context = self.consult(last_sentences[0], self.context.__getitem__(len(self.context) - 1))

        self.context.append(new_context)

    def defSentences(self, raw_sentence: str):
        self.raw_sentence = raw_sentence
        processed_sentences = list()

        nlp = spacy.load("es_core_news_lg")

        doc = nlp(self.raw_sentence)

        sentencias = list(doc.sents)

        for sentencia in sentencias:
            conjuntoHead = set()
            conjuntoVERB = set()
            conjuntoPROPN = set()
            conjuntoADJ = set()
            conjuntoNOUN = set()
            conjuntoNUM = set()
            listaEntidades = list()
            for ent in sentencia.ents:
                listaEntidades.append([ent.text, ent.label_])
            for token in sentencia:
                conjuntoHead.add(token.head.text)
                if token.pos_ == "VERB":
                    conjuntoVERB.add(token.lemma_)
                if token.pos_ == "PRONP":
                    conjuntoPROPN.add(token.lemma_)
                if token.pos_ == "ADJ":
                    conjuntoADJ.add(token.lemma_)
                if token.pos_ == "NOUN":
                    conjuntoNOUN.add(token.lemma_)
                if token.pos_ == "NUM":
                    conjuntoNUM.add(token.lemma_)

            processed_sentences.append(
                Sentence(conjuntoVERB, conjuntoADJ, listaEntidades, conjuntoPROPN, conjuntoNOUN, conjuntoNUM))

        return processed_sentences

    def consult(self, sentence: Sentence, context: Context):
        # Ciertas condiciones para llevar a cabo la gestion de consultas a la KB.
        # TODO falta esto, logica de seleccion de aima y generacion de preguntas y nuevos contextos
        return None
