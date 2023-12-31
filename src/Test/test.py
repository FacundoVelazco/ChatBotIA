import spacy
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("es_core_news_lg")
lenguajes = ["Python", "Java", "C++", "JavaScript", "Ruby", "Swift", "Go", "Rust", "PHP", "Haskell", "C#", "Perl",
             "Objective-C","TypeScript", "Kotlin", "Scala", "R", "Lua", "Matlab", "Groovy", "Clojure", "Shell",
             "HTML","CSS", "SQL", "Assembly","F#", "Elixir", "Dart", "Julia", "Racket", "Fortran", "VB.NET",".Net"]

lenguajes_patterns = list(nlp.pipe(lenguajes))
print("patrones_de_lenguajes:", lenguajes_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("LENGUAJES", None, *lenguajes_patterns)


# Define el componente personalizado
@Language.component("lenguajes_component")
def lenguajes_component_function(doc):
    # Aplica el matcher al doc
    matches = matcher(doc)
    # Crea un Span para cada resultado y asígnales el label "LENGUAJES"
    spans = [Span(doc, start, end, label="LENGUAJES") for match_id, start, end in matches]
    # Sobrescribe los doc.ents con los spans resultantes
    doc.ents = spans
    return doc


# Añade el componente al pipeline después del componente "ner"
#nlp.add_pipe("lenguajes_component", after="ner")
#print(nlp.pipe_names)

# Procesa el texto e imprime en pantalla el texto y el label
# de los doc.ents

doc = nlp("Un programador tiene una premonición de que vive programando haciendo programas para poder promocionar una materia. Aveces soñaba que programaba dentro de un programa")

#doc = nlp("Actualmente estoy viviendo en Santa fe, Argentina, me gustaría vivir en San Pablo, Brasil")

print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

doc2 = nlp("programar")
tokenObjetivo = doc2[0]


print([(ent.text, ent.label_) for ent in doc.ents])
for token in doc:
    if token.text == "no" or not token.is_stop:
        #print(token.lemma_, "\tPOS", token.pos_, "\tTAG", token.tag_, "\tDEP", token.dep_)
        if (tokenObjetivo.similarity(nlp(token.lemma_)[0]) >= 0.5):
            print(token.text,">",token.lemma_,"<->", tokenObjetivo.text)
print("------Entidades y label-------------")
for entidad in doc.ents:
    print("\tPalabra", entidad.text, "\tLabel", entidad.label_)


