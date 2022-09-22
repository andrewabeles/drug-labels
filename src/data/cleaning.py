from string import punctuation

def process_data(drugs_raw):
    """Process the raw drugs data.
    
    Takes the raw drugs dataframe as input and performs some basic column reformatting and text processing like tokenization.
    """
    drugs_processed = drugs_raw.copy()
    drugs_processed['warnings'] = drugs_processed['warnings'].apply(lambda x: ' '.join(eval(x))) # transform warnings from list of strings to single string
    drugs_processed['openfda.product_type'] = drugs_processed['openfda.product_type'].apply(lambda x: eval(x)[0]) # transform product type from list to single string
    drugs_processed.rename(columns={'openfda.product_type': 'product_type'}, inplace=True) # rename product_type column 
    drugs_processed = drugs_processed.query("warnings != ''").reset_index(drop=True) # remove rows with blank warnings 
    drugs_processed['tokens'] = drugs_processed['warnings'].apply(prepare) # apply text processing to warnings 
    return drugs_processed[['warnings', 'tokens', 'product_type']]

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