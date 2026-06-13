import nltk
from nltk.tokenize import word_tokenize
text = """The curious student carried a notebook through the quiet library and carefully read an interesting book about science, while the helpful teacher explained difficult concepts with clear examples. A bright lamp on the wooden table provided enough light, and every attentive learner completed the assigned task successfully."""

# print(text)

#extract words
words = word_tokenize(text)
print(words)

#extract pos 
pos_tags = nltk.pos_tag(words)
print("POS Tags ",pos_tags)



