# -------------------
#  Copyright (c) 2023.
#  el copicopi
# -------------------
# Archivo inicial del programa, la idea seria realizar ciclos de percepcion accion
# donde el bot obtenga informacion del usuario durante la sesion y la almacene en su KB
# cuando tenga su KB consistente podra recomendar cosas al usuario.
# El resultado de una sesion seria una recomendacion laboral al usuario.
# Me parece interesante tratar cada charla como una sesion, con informacion temporal de esa sesion.
# -------------------
# Para empezar podemos analizar el texto con spacy.
# Con los tokens generados podemos realizar un analisis mediante LPO,
# viendo que tokens se encuentran en nuestra KB. A medida que encontremos
# informacion del usuario podemos ir agregandola a la KB de una manera similar a:
# (Si el usuario ingresara java y algun verbo) Sabemos : lenguaje(java),
# Inferimos: programaEn(usuario,java).
# De esta mmanera tenemos nuevo conocimiento. Habria que pensar bien como vamos
# a hacer toodo esto, pero la base esta.
# -------------------
# Podriamos usar la api de telegram para conectarnos y hablarle al bot por ahi.


# Para correr el programa
# pip install -U spacy
# python -m spacy download en_core_web_lg
# Important:: chequear bien que version de python se esta utilizando y que interprete,
# muchas veces la version de terminal de comandos no es la misma que la de ejecucion en pycharm u otro IDE.

from Classes.Manager import Manager

def main():
    manager = Manager()

    manager.start()

    # Load English tokenizer, tagger, parser and NER
    # nlp = spacy.load("es_core_news_lg")
    #
    # mensajesBienvenida()
    #
    # while True:
    #     user_input = input("-- ")
    #
    #     if user_input == "x":
    #         print("¡¡Adios!!")
    #         break
    #
    #     ##Para cuando queramos trabajar con negaciones/afirmaciones.
    #     #doc = nlp(user_input.replace("No ", " negar ").replace(" no ", " negar ").replace("Si ", " afirmar ").replace(" si "," afirmar "))
    #     # Analyze syntax
    #     #      print("Sustantivos:", [chunk.text for chunk in doc.noun_chunks])
    #     #      print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
    #     #      print("Entidades", doc.ents)
    #
    #     doc = nlp(user_input)
    #     print("Lista sentencias ::")
    #     sentencias = list(doc.sents)
    #     for sentencia in sentencias:
    #         print("Sentencia :: ----------------------")
    #         conjuntoHead = set()
    #         conjuntoVERB = set()
    #         conjuntoPROPN = set()
    #         conjuntoADJ = set()
    #         conjuntoNOUN = set()
    #         conjuntoNUM = set()
    #         listaEntidades = list()
    #         for ent in sentencia.ents:
    #             listaEntidades.append([ent.text,ent.label_])
    #         for token in sentencia:
    #             conjuntoHead.add(token.head.text)
    #             if token.pos_ == "VERB" :
    #                 conjuntoVERB.add(token.lemma_)
    #             if token.pos_ == "PRONP":
    #                 conjuntoPROPN.add(token.lemma_)
    #             if token.pos_ == "ADJ":
    #                 conjuntoADJ.add(token.lemma_)
    #             if token.pos_ == "NOUN":
    #                 conjuntoNOUN.add(token.lemma_)
    #             if token.pos_ == "NUM":
    #                 conjuntoNUM.add(token.lemma_)
    #         print(conjuntoHead)
    #         print(conjuntoVERB)
    #         print(conjuntoPROPN)
    #         print(conjuntoADJ)
    #         print(conjuntoNOUN)
    #         print(conjuntoNUM)
    #         print(listaEntidades)


def mensajesBienvenida():
    print("------------------------------------")
    print("Bienvenido al agente virtual de RRHH")
    print("  ")
    print("Lo guiaré en la ardua tarea de encontrar una posición de trabajo dentro del sector IT")
    print("------------------------------------")
    print("¿Como se encuentra el dia de hoy?")


if __name__ == '__main__':
    main()
