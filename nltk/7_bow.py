from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "The cat sat on the mat",
    "The dog sat on the log",
    "The cat chased the mouse",
    "The dog chased the cat"
]
print(documents)

#create object of CountVectorizer
cv = CountVectorizer()

bag_of_words = cv.fit_transform(documents)

print("Vocabulary ",cv.vocabulary_)
print("Matrix",bag_of_words.toarray())
