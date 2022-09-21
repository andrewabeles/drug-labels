from string import punctuation

def make_interim_data(drugs_raw):
    """Perform some basic processing on the raw drugs data.
    
    Takes the raw drugs dataframe as input and performs some basic column selection and reformatting. The output is considered interim 
    (not processed) because the function does not do any text processing.
    """
    drugs_interim = drugs_raw[['warnings', 'openfda.product_type']].copy() # filter for the columns of interest
    drugs_interim['warnings'] = drugs_interim['warnings'].apply(lambda x: ' '.join(eval(x))) # transform warnings from list of strings to single string
    drugs_interim['openfda.product_type'] = drugs_interim['openfda.product_type'].apply(lambda x: eval(x)[0]) # transform product type from list to single string
    drugs_interim.rename(columns={'openfda.product_type': 'product_type'}, inplace=True) # rename product_type column 
    drugs_interim.dropna(inplace=True) # remove rows with missing values 
    return drugs_interim

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