import spacy
from spacy.language import Language
from spacy.tokens import Doc
import re

# Create custom extensions
Doc.set_extension("has_email", default=False)
Doc.set_extension("emails", default=[])

@Language.component("email_extractor")
def email_extractor(doc):
    text = doc.text
    
    # ✅ FIXED: Removed ^ and $ anchors
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all emails (case insensitive)
    found_emails = re.findall(email_pattern, text, re.IGNORECASE)
    if len(found_emails) > 0:
        doc._.has_email = True
        doc._.emails = found_emails
    
    return doc


# Test sentence
sentence = """Hello my name is ankit patel. and you can send me email on ankit3385@gmail.com. 
my other email address is theeasylearn@gmail.com"""

# Load spacy and add custom component
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("email_extractor", last=True)

doc = nlp(sentence)

print("\nHas Email:", doc._.has_email)
print("Emails:", doc._.emails)