'''
Dictionary 
    Dictionary 
        List 
            Dictionary
                id,topic,title,keyword(list),overview,utterances(list),answer,answer_variation(list)
'''
question = "fees"
import knowledge_base as k 
subjects = k.knowledge.get('knowledge_base') #return list 
# print(topics)
for subject in subjects:
    # print(subject.get('keywords'))
    # print(subject.get('answer'))
    # print("_"*100)
    if question in subject.get('keywords'):
       print(subject.get('answer'))
        
