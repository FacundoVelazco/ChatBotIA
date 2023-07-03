from Classes.EnumContextNames import ContextName


def getQuestions():
    questions = list()
    # TODO añadir mas preguntas con contextos
    # Questions:: pares del estilo [contexto,pregunta]. EJ: [PRESENTACION, Hola ¿Como te llamas?];
    # EJ: [LEGUAJES,¿Que lenguajes de programacion conoce?]

    questions.append([ContextName.PRESENTACION, "Hola ¿Como te llamas?"])
    questions.append([ContextName.LENGUAJE, "En que Leguaje o framework ha trabajado?"])
    questions.append([ContextName.LOCACION, "En que pais o Ciudad le gustaria trabajar?"])
    questions.append([ContextName.IDIOMA, "Posee manejo de alguna lengua extranjera? En que Idioma?"])
    questions.append([ContextName.MODALIDAD, "Posemos 3 tipos de modalidad de trabajo, Presencial, remoto o Mixto, cual es de su preferencia?"])
    questions.append([ContextName.DISPONIBILIDAD, "Que Disponibilidad horaria posee para el trabajo? (Part-time / Full-time / Freelance)"])
    questions.append([ContextName.EQUIPO, "Participó en algún equipo de trabajo? Cual fue su rolo en el mismo? (Lider/ Referente/ Colaborador)"])
    questions.append([ContextName.EQUIPO, "Ha Gestionado multiples equipos de trabajo? (Lider/ Colaborador)"])
    questions.append([ContextName.ARQUITECTURA, "Está familiarizado con las arquitecturas Cloud y/o On-premise? (Cloud / On-premise)"])
    questions.append([ContextName.SUELDO, "Que nivel se sueldo espera percibir? (Bajo/Medio/Alto)"])
    questions.append([ContextName.CEO, "Durante su carrera en IT, ha tenido que tomar desiciones estatégias y/o técnicas a nivel departamental y/o organizacional? ( Si/No)"])



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
