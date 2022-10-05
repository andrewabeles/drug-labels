from string import punctuation
import re

def remove_punctuation(text):
    punct_set = set(punctuation)
    punct_set.remove('/') # keep '/' to use for tokenization
    return "".join([char for char in text if char not in punct_set])

def remove_numbers(text):
    pattern = re.compile(r'[0-9]+')
    return re.sub(pattern, '', text)

def tokenize(text):
    pattern = re.compile(r'[\s/]') # split on whitespace and '/'
    tokens = re.split(pattern, text)
    tokens = [t for t in tokens if t != ''] # remove blank tokens that used to be '/'
    return tokens

def remove_stopwords(tokens):
    """ToDo"""
    return tokens

def prepare(text, pipeline=[str.lower, remove_punctuation, tokenize, remove_stopwords]):
    """Pass a string through a text processing pipeline."""
    for transform in pipeline:
        text = transform(text)
    return text