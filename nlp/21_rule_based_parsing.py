import spacy as sa
from spacy.matcher import Matcher

nlp = sa.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)

text = "Apple is buying uk based startup for $1 billion. Tesla has bought one company in Australia."

doc = nlp(text)

pattern = [
    {"LOWER": {"IN": ["apple", "tesla"]}},
    {"POS": "AUX", "OP": "*"},
    {"LEMMA": "buy"}
]

matcher.add("company", [pattern])

matches = matcher(doc)

for match_id, start, end in matches:
    print(doc[start:end])