# Named Entity Recognition (NER) Project

This project demonstrates Named Entity Recognition (NER) using the **spaCy** NLP library. It identifies and classifies named entities (such as persons, organizations, locations, dates, etc.) in text.

## Features

- Identify named entities in a given text.
- Classify entities into categories (e.g., PERSON, ORG, GPE, DATE).
- Use pre-trained spaCy models.
- Optional visualization of named entities using spaCy's `displaCy`.

## Prerequisites

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/ner-spacy-project.git
   ```

2. Install the required dependencies:

   ```bash
   pip install spacy
   python -m spacy download en_core_web_sm
   ```

## Usage

1. **Run the script**:

   To extract named entities from a sample text:

   ```bash
   python ner_spacy.py
   ```

2. **Input Text**:

   Replace the `text` variable in the script with any text you want to process for named entities.

3. **Displaying Named Entities**:

   The script will print the extracted named entities and their corresponding labels (e.g., PERSON, ORG, etc.).

4. **Visualization**:

   If you're using Jupyter Notebook, you can visualize the entities using spaCy's `displaCy` tool:

   ```python
   displacy.render(doc, style="ent", jupyter=True)
   ```

   For web-based visualization, uncomment the following line:

   ```python
   displacy.serve(doc, style="ent")
   ```

### Example

Input text:

```text
Apple Inc. is an American multinational technology company headquartered in Cupertino, California. It was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976. Tim Cook is the current CEO. The company was valued at over $1 trillion as of 2018.
```

Output:

```bash
Named Entities in the text:
------------------------------
Apple Inc. (ORG)
American (NORP)
Cupertino (GPE)
California (GPE)
Steve Jobs (PERSON)
Steve Wozniak (PERSON)
Ronald Wayne (PERSON)
1976 (DATE)
Tim Cook (PERSON)
CEO (ORG)
$1 trillion (MONEY)
2018 (DATE)
```

## Customization

- **Text Input**: Replace the sample text with your own input to extract named entities.
- **NER Models**: You can experiment with other spaCy models or train a custom NER model by following spaCy's documentation on [training a new entity type](https://spacy.io/usage/training#ner).

## Dependencies

- Python 3.x
- spaCy

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

### Author

Developed by [Duncan Abonyo](https://github.com/duncanodhis).

---

