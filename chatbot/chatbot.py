import knowledge_base as k 
import spacy 
nlp = spacy.load('en_core_web_sm')
agent = "Skisha: "
subjects = k.knowledge.get('knowledge_base') #return list 
def preprocess(question):
    isFound = False
    for item in k.greetings:
        if question == item.get('message'):
            print(agent,item.get('reply'))
            return 
       
    global subjects
    doc = nlp(question)
    for subject in subjects:
        if question in subject.get('utterances'):
            print(subject.get('answer'))
            return
        
    for token in doc:
        for subject in subjects:
            if token.text in subject.get('keywords'):
                #print(token,subject.get('keywords'))
                print(subject.get('answer'))
                isFound = True
                break

    if isFound == False:
        print(agent,"sorry i dont have answer of your question")
while True:
    question = input("You : ")
    if question == "bye" or question == "exit":
        print(agent," Good bye see you again,")
        break 
    else:    
        preprocess(question)