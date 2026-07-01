import spacy as sa 
nlp = sa.load('en_core_web_sm')
text = """Wow although I met Dr. Priya in Ahmedabad on July 1 2026 she quickly analyzed my beautifully written English report about artificial intelligence and robotics because every student who attended eagerly asked intelligent questions while others quietly observed the demonstration with three laptops two tablets costing ₹50000 each yet nobody complained despite heavy rain or traffic however we successfully completed 95% of tasks before sunset then everyone celebrated happily at Riverfront Cafe where children sang songs and parents smiled warmly if anyone emailed team@example.com or visited https://example.com they found useful educational resources immediately afterwards for future research and collaboration always."""

doc = nlp(text)

print(f"{'token':<12} {'leema':<12} {'POS':<12} {'Fine POS':<12} {'Dependency':<12} {'entity':<12} {'stop':<12}")
print("-"*12)
for token in doc:
    print(f"{token.text:<12} {token.lemma_:<12} {token.pos_:<12} {token.tag_:<12} {token.dep_:<12}{token.ent_type_:<12} {token.is_stop:<12}")
