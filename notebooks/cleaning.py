from string import punctuation
import re
import nltk
from nltk.corpus import stopwords

### VARIABLES ###

# punctuation 
punct_set = set(punctuation)
punct_set.remove('/') # keep '/' to use for tokenization

# numbers  
numbers_pattern = re.compile(r'[0-9]+')

# tokenization  
token_pattern = re.compile(r'[\s/]') # split on whitespace and '/'
    
# stopwords  
nltk.download('stopwords')
stopwords_set = set(stopwords.words('english'))
additional_stopwords = ['dosage', 'administration', 'directions', '•']
for sw in additional_stopwords:
    stopwords_set.add(sw)
    
### FUNCTIONS ###

def remove_punctuation(text):
    return "".join([char for char in text if char not in punct_set])

def remove_numbers(text):
    return re.sub(numbers_pattern, '', text)

def tokenize(text):
    tokens = re.split(token_pattern, text)
    tokens = [t for t in tokens if t != ''] # remove blank tokens that used to be '/'
    return tokens

def remove_stopwords(tokens):
    return [t for t in tokens if t not in stopwords_set]

def prepare(text, pipeline=[str.lower, remove_punctuation, remove_numbers, tokenize, remove_stopwords]):
    """Pass a string through a text processing pipeline."""
    for transform in pipeline:
        text = transform(text)
    return text

def get_document_features(tokens, featureset):
    return {t: t in featureset for t in tokens}