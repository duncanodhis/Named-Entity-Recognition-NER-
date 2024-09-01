import spacy

# Load the pre-trained model
nlp = spacy.load("en_core_web_sm")

# Sample text 
text = """
Apple Inc. is an American multinational technology company headquartered in Cupertino, California. 
It was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976. 
Tim Cook is the current CEO. The company was valued at over $1 trillion as of 2018.
"""

# Process the text using the NLP model
doc = nlp(text)

# Function to display named entities
def display_named_entities(doc):
    print(f"\nNamed Entities in the text:\n{'-'*30}")
    for ent in doc.ents:
        print(f"{ent.text} ({ent.label_})")

# Display the named entities and their types
display_named_entities(doc)

# Optionally visualize the entities using displaCy (for Jupyter Notebook or web)
try:
    from spacy import displacy
    displacy.render(doc, style="ent", jupyter=True)  # For Jupyter Notebooks
    # displacy.serve(doc, style="ent")  # Uncomment to run in a web browser
except ImportError:
    print("displaCy is only available in Jupyter or as a web server.")
