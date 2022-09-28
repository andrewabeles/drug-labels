from string import punctuation

def process_data(drugs_raw):
    """Process the raw drugs data.
    
    Takes the raw drugs dataframe as input and performs some basic column reformatting and text processing like tokenization.
    """
    drugs_processed = drugs_raw.copy()
    drugs_processed['target'] = drugs_processed['openfda.route'].apply(lambda x: eval(x)[0]) # transform column from list to single string
    drugs_processed.dropna(subset=['dosage_and_administration'], inplace=True) # drop rows missing the text field 
    drugs_processed['text'] = drugs_processed['dosage_and_administration'].apply(lambda x: ' '.join(eval(x))) # transform column from list of strings to single string
    drugs_processed = drugs_processed.query("text != ''").reset_index(drop=True) # remove rows with blank text 
    drugs_processed['tokens'] = drugs_processed['text'].apply(prepare) # apply text processing 
    return drugs_processed[['target', 'text', 'tokens']]

def remove_punctuation(text):
    punct_set = set(punctuation)
    return "".join([char for char in text if char not in punct_set])

def tokenize(text):
    return text.split()

def remove_stopwords(tokens):
    """ToDo"""
    return tokens

def prepare(text, pipeline=[str.lower, remove_punctuation, tokenize, remove_stopwords]):
    """Pass a string through a text processing pipeline."""
    for transform in pipeline:
        text = transform(text)
    return text