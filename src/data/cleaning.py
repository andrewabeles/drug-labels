from string import punctuation

def make_processed_data(drugs_interim):
    """ToDo. Vectorize the interim drugs data for modeling."""
    return drugs_interim

def make_interim_data(drugs_raw):
    """Perform some basic processing on the raw drugs data.
    
    Takes the raw drugs dataframe as input and performs some basic column reformatting and text processing. The output is considered interim 
    because it is not yet vectorized.
    """
    drugs_interim = drugs_raw.copy()
    drugs_interim['warnings'] = drugs_interim['warnings'].apply(lambda x: ' '.join(eval(x))) # transform warnings from list of strings to single string
    drugs_interim['openfda.product_type'] = drugs_interim['openfda.product_type'].apply(lambda x: eval(x)[0]) # transform product type from list to single string
    drugs_interim.rename(columns={'openfda.product_type': 'product_type'}, inplace=True) # rename product_type column 
    drugs_interim = drugs_interim.query("warnings != ''").reset_index(drop=True) # remove rows with blank warnings 
    drugs_interim['tokens'] = drugs_interim['warnings'].apply(prepare) # apply text processing to warnings 
    return drugs_interim[['warnings', 'tokens', 'product_type']]

def remove_punctuation(text):
    punct_set = set(punctuation)
    return "".join([char for char in text if char not in punct_set])

def tokenize(text):
    return text.split()

def remove_stopwords(tokens):
    """ToDo"""
    return tokens

def prepare(text, pipeline=[str.lower, remove_punctuation, tokenize, remove_stopwords]):
    for transform in pipeline:
        text = transform(text)
    return text