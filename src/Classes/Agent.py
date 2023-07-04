from Classes.Sentence import Sentence
from Classes.LogicUtil import LogicUtil
from Classes.Context import Context
from Classes.EnumContextNames import ContextName
from Classes.Utils import normalizer, successCheck
import spacy


class Agent:
    def __init__(self):
        self.raw_sentence = list()
        self.context = list()
        self.sentence = list()
        self.aima = LogicUtil()
        init_context = Context(ContextName.PRESENTACION.name)
        self.context.append(init_context)

    def getLastContext(self):
        return self.context.__getitem__(len(self.context) - 1)

    def addRawSentence(self, text: str):
        self.raw_sentence.append(text)

    def getAnswer(self):
        if len(self.raw_sentence) == 0:
            return ["Use addRawSentence first...", ""]

        # Cadena ingresada por el usuario
        last_raw_sentence = self.raw_sentence.__getitem__(len(self.raw_sentence) - 1)
        # Cadenas procesada por spacy
        last_sentences = self.defSentences(last_raw_sentence)
        # TODO por ahora solo usamos la primer sentencia que nos envian, por una cuestion de simplificar el problema,
        #  se podria ampliar luego
        self.sentence.append(last_sentences[0])
        # Creamos un contexto nuevo y lo devolvemos.
        new_context = self.consult(self.aima, last_sentences[0], self.context.__getitem__(len(self.context) - 1))

        self.context.append(new_context)

    def defSentences(self, raws: str):
        raw_sentence = raws
        processed_sentences = list()

        nlp = spacy.load("es_core_news_lg")

        doc = nlp(raw_sentence)

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
                listaEntidades.append(ent)
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

    def consult(self, aima: LogicUtil, sentence: Sentence, context: Context):
        # Consultar exito
        success_list = successCheck(aima)
        if len(success_list) > 0:
            final_answer = "Muchas gracias por responder a las preguntas, los puestos que tenemos disponibles para usted son : "
            for element in success_list:
                if success_list.index(element) == len(success_list) - 1:
                    final_answer = final_answer + element + "."
                else:
                    final_answer = final_answer + element + ", "

            return Context(ContextName.EXITO.name, final_answer)

        if context.context_name == ContextName.PRESENTACION.name:
            for entity in sentence.entidades:
                if entity.label_ == "PER":
                    aima.tell("Usuario(" + normalizer(entity.text) + ")")
                    return Context(ContextName.MODALIDAD.name)

        if context.context_name == ContextName.MODALIDAD.name:
            for adj in sentence.adjetivos:
                clausulaModalidad = "Modalidad(" + normalizer(adj) + ")"
                if aima.askConditional(clausulaModalidad):
                    aima.tell("ModalidadUser(" + normalizer(adj) + ")")
                    break

            opcionesLocacion = ["Presencial", "Mixto"]
            opcionesDisponibilidad = ["Virtual", "Remoto"]
            res = aima.ask("ModalidadUser(x)")
            if type(res) != bool:
                for adj in res.values():
                    if opcionesLocacion.count(normalizer(adj.__str__())):
                        return Context(ContextName.LOCACION.name)
                    if opcionesDisponibilidad.count(normalizer(adj.__str__())):
                        return Context(ContextName.DISPONIBILIDAD.name)

        if ContextName.LOCACION.name == context.context_name:
            found = False
            for entity in sentence.entidades:
                clausulaCiudad = "Ciudad(" + normalizer(entity.text) + ")"
                clausulaPais = "Pais(" + normalizer(entity.text) + ")"
                if aima.askConditional(clausulaPais):
                    aima.tell("UserPais(" + normalizer(entity.text) + ")")
                    found = True
                    break
                if aima.askConditional(clausulaCiudad):
                    aima.tell("UserCiudad(" + normalizer(entity.text) + ")")
                    found = True
                    break
            if found:
                return Context(ContextName.DISPONIBILIDAD.name)

        if ContextName.DISPONIBILIDAD.name == context.context_name:
            for entity in sentence.entidades:
                clausulaDisponibilidad = "Disponibilidad(" + normalizer(entity.text) + ")"
                if aima.askConditional(clausulaDisponibilidad):
                    aima.tell("DisponibilidadUser(" + normalizer(entity.text) + ")")
                    return Context(ContextName.LENGUAJE.name)

        if ContextName.LENGUAJE.name == context.context_name:
            for entity in sentence.entidades:
                clausulaLenguaje = "Lenguaje(" + normalizer(entity.text) + ")"
                if aima.askConditional(clausulaLenguaje):
                    aima.tell("LengUser(" + normalizer(entity.text) + ")")
                    return Context(ContextName.EQUIPO.name)

        if ContextName.EQUIPO.name == context.context_name:
            for entity in sentence.entidades:
                clausulaEquipo = "TrabajoenEquipo(" + normalizer(entity.text) + ")"
                if aima.askConditional(clausulaEquipo):
                    aima.tell("RolEquipoUser(" + normalizer(entity.text) + ")")
                    return Context(ContextName.IDIOMA.name)

        if ContextName.IDIOMA.name == context.context_name:
            for entity in sentence.entidades:
                clausulaIdioma = "Idioma(" + normalizer(entity.text) + ")"
                if aima.askConditional(clausulaIdioma):
                    aima.tell("IdiomasUser(" + normalizer(entity.text) + ")")
                    # TODO modificar este ultimo retorno, fuerza el final.
                    return Context(ContextName.FINAL.name)

        # if ContextName.CEO.name == context.context_name:
        #    for entity in sentence.entidades:
        #        clausulaCEO = "Metas(" + normalizer(entity.text) + ")"
        #        if aima.askConditional(clausulaCEO):
        #            aima.tell("MetasUser(" + normalizer(entity.text) + ")")
        #            return Context(ContextName.FINAL.name)

        return context
