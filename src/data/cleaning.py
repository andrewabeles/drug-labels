def make_interim_data(drugs_raw):
    """Perform some basic processing on the raw drugs data.
    
    Takes the raw drugs dataframe as input and returns an interim dataframe. The output is interim (not clean) because
    the function does not do any text processing, just basic column selection and reformatting.
    """
    drugs_interim = drugs_raw[['warnings', 'openfda.product_type']].copy() # filter for the columns of interest
    drugs_interim['warnings'] = drugs_interim['warnings'].apply(lambda x: ' '.join(eval(x))) # transform warnings from list of strings to single string
    drugs_interim['openfda.product_type'] = drugs_interim['openfda.product_type'].apply(lambda x: eval(x)[0]) # transform product type from list to single string
    drugs_interim.rename(columns={'openfda.product_type': 'product_type'}, inplace=True) # rename product_type column 
    return drugs_interim