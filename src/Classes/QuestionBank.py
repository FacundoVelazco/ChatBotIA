from EnumContextNames import ContextName


def getQuestions():
    questions = list()
    # TODO añadir mas preguntas con contextos
    # Questions:: pares del estilo [contexto,pregunta]. EJ: [PRESENTACION, Hola ¿Como te llamas?];
    # EJ: [LEGUAJES,¿Que lenguajes de programacion conoce?]

    questions.append([ContextName.PRESENTACION, "Hola ¿Como te llamas?"])

    return questions


def find(context_name: str):
    questions = getQuestions()
    match_questions = list()
    for question in questions:
        if question[0].name == context_name:
            match_questions.append(question)
    match_questions.sort()

    if len(match_questions) == 0: return list()

    return match_questions[0]
