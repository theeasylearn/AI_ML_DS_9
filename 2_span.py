import spacy as sa 
nlp = sa.load('en_core_web_sm')

text = "we have started using spacy in nlp"
#create doc object
doc = nlp(text)

#create span object (span group of tokens)
span_1 = doc[0:3] #we have started
span_2 = doc[3:5] # using spacy 
span_3 = doc[5:] #  spacy in nlp 
print(span_1)
print(span_2)
print(span_3)
