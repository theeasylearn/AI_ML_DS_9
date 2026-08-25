import spacy as sa 
nlp = sa.load('en_core_web_sm')

text = """Natural Language Processing (NLP) is a branch of Artificial Intelligence (AI) that enables computers to understand, interpret, analyze, and generate human language. It combines techniques from computer science, linguistics, and machine learning to process text and speech in a meaningful way. 123 abc123

NLP is widely used in real-world applications such as chatbots, virtual assistants, language translation, sentiment analysis, spam detection, text summarization, and search engines. It allows machines to extract useful information from unstructured text and communicate with users in a natural and intelligent manner."""
#create doc object
doc = nlp(text)

for token in doc:
    lexeme = token.lex
    print("lexeme in lower",lexeme.lower_)
    print("is this alphabet ",lexeme.is_alpha)
    print("is this digit ",lexeme.is_digit)
    print("is this punctuation  mark",lexeme.is_punct)
    print("is this alpha numeric ",lexeme.like_num)