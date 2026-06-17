import nltk
from nltk.tokenize import word_tokenize

# Your text
text = "Yesterday, Rohan Patel traveled from Bhavnagar to Ahmedabad to attend a technology conference organized by The Easylearn Academy. During the event, he met Priya Shah, a software engineer from Infosys, and Michael Johnson, a researcher from Stanford University. They discussed artificial intelligence projects funded by Google and Microsoft with a budget of ₹50 lakh. The conference was held on 15 June 2026 at the Mahatma Mandir Convention Centre in Gandhinagar, Gujarat, India. Later, the team booked rooms at the Taj Hotel and planned a visit to New Delhi before flying to the United States on 20 June 2026."

# Tokenization
tokens = word_tokenize(text)

# POS Tagging
pos_tags = nltk.pos_tag(tokens)

# NER Chunking
ner_tree = nltk.ne_chunk(pos_tags)

# Function to extract only Named Entities
def extract_entities(tree):
    entities = []
    for chunk in tree:
        if hasattr(chunk, 'label'):  # It's a named entity chunk
            entity = ' '.join(c[0] for c in chunk)  # Join words in the entity
            entity_type = chunk.label()             # PERSON, ORGANIZATION, GPE, etc.
            entities.append((entity, entity_type))
    return entities

# Get entities
named_entities = extract_entities(ner_tree)

# Print only NER
print("Named Entities Found:")
for entity, entity_type in named_entities:
    print(f"{entity} --> {entity_type}")
    