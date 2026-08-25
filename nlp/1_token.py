import spacy as sa 
#create nlp object
nlp = sa.load('en_core_web_sm') 


text = """On 18 March 2026 at 10:00 AM PDT, NVIDIA hosted its annual developer conference in San Jose, where it unveiled the NVIDIA Blackwell Ultra platform for next-generation AI workloads. The company announced that the new system would start at US$39,999 (USD) for enterprise configurations, attracting developers, researchers, and business leaders from around the world.
"""
#create doc object 
doc = nlp(text)
for token in doc: #for loop will run for each and every token 
    print(token)

#detect entities (person, company, place, date & time currency product)
print("-"*100)
for entity in doc.ents:
    print(entity.text,entity.label_)
