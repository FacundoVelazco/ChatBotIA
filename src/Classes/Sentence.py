

class Sentence:
    def __init__(self,verbos:set,adjetivos:set,entidades:list,pronombres:set,sustantivos:set,numericos:set):
        self.verbos = verbos
        self.adjetivos = adjetivos
        self.entidades = entidades
        self.pronombres = pronombres
        self.sustantivos = sustantivos
        self.numericos = numericos
