import spacy


class Sentence:
    def __init__(self, raw_sentence: str):
        self.raw_sentence = raw_sentence

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
