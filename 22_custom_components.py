import spacy 
from spacy.language import Language
from spacy.tokens import Doc 

#create list that has few it course name
trending_it_courses = ["Artificial Intelligence & Machine Learning", "Cloud Computing & DevOps", "Cybersecurity & Digital Risk", "Data Science & Advanced Analytics", "Full-Stack Software Engineering", "Agentic AI & Prompt Engineering", "Model Context Protocol (MCP) Development", "Blockchain Technology & Smart Contracts", "Product Platform Engineering", "Business Intelligence & Data Engineering","Python"]

#create property/extension
Doc.set_extension("courses",default=[])

@Language.component("course_finder")
def course_finder(doc):
    text = doc.text.lower()
    print("I have been executed automatically")
    asked_courses = []
    for item in trending_it_courses:
        if item.lower() in text:
            asked_courses.append(item)
    doc._.courses = asked_courses #copy found courses into courses
    return doc 

question = """I am looking to enroll in a program that covers Python , Artificial Intelligence & Machine Learning to help me build the right skills for a career in the tech industry."""

#create nlp object
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("course_finder",last=True)
doc = nlp(question)
print(doc._.courses)