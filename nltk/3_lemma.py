from nltk.stem import WordNetLemmatizer

#crete object of the class 
lemma = WordNetLemmatizer()

adjectives = ["worst", "fastest", "longest", "highest", "happy", "jolly", "keen", "lively", "mighty", "noble","better"]

verbs = ["running", "swimming", "playing", "jumping", "climbing", "dancing", "hiking", "cycling", "skating", "surfing"]

for item in adjectives:
    print(lemma.lemmatize(item,pos='a'))
print("_"*100)
for item in verbs:
    print(lemma.lemmatize(item,pos='v'))
