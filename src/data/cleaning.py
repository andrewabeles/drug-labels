def clean_drugs(drugs_raw):
    drugs_clean = drugs_raw[['warnings', 'openfda.product_type']]
    drugs_clean['warnings'] = drugs_clean['warnings'].apply(lambda x: ' '.join(x)) # transform warnings from list of strings to single string
    drugs_clean['product_type'] = drugs_clean['openfda.product_type'].apply(lambda x: x[0]) # transform product type from list to single string 
    return drugs_clean 