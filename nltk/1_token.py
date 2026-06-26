import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
nltk.download('punkt_tab')
text = """Natural Language Processing (NLP) is a branch of Artificial Intelligence that enables computers to understand, interpret, and generate human language. It is used in applications such as chatbots, language translation, sentiment analysis, and speech recognition. NLP helps machines process text and speech efficiently, making human-computer interaction more natural and effective."""

print(text)

#extract words
words = word_tokenize(text)
print(words)

#extract sentences 
sentences = sent_tokenize(text)
print(sentences)

