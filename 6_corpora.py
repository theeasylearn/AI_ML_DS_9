import nltk

from nltk.corpus import gutenberg
print(gutenberg.fileids())
story = gutenberg.words('milton-paradise.txt')
print("no of words in story ",len(story))

#print 1st 50 words
print(story[0:50])