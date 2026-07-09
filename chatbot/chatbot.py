import knowledge_base as k 
import spacy 
agent = "Skisha: "
while True:
    question = input("You : ")
    for item in k.greetings:
        if question == item.get('message'):
            print(agent,item.get('reply'))
    if question == "bye" or question == "exit":
        print(agent," Good bye see you again,")
        break 