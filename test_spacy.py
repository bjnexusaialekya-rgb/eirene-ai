import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Eirene AI understands human emotion.")

for token in doc:
    print(token.text, token.pos_)