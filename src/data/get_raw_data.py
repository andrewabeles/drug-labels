import requests
import re 
import pandas as pd

def get_all_drugs(url, all_drugs=[]):
    """Get list of drugs from OpenFDA API.  
    
    Given a query URL, this function recursively calls the OpenFDA API and returns a list of dictionaries representing 
    all drugs returned by the query.
    """
    r = requests.get(url)
    if r.status_code == 200:
        drugs = r.json()['results']
        all_drugs.extend(drugs)
        if 'Link' in r.headers:
            url = re.findall(r'<(.*)>', r.headers['Link'])[0] # extract the next page's url from response header
            return get_all_drugs(url, all_drugs) # recursively pass it through the function
        else: # the last page of results does not include a Link in the header 
            return all_drugs

url = 'https://api.fda.gov/drug/label.json?search=_exists_:warnings+AND+_exists_:openfda.product_type&limit=1000'
drugs = get_all_drugs(url) # get list of drugs 
df = pd.json_normalize(drugs) # store them in a pandas dataframe 
df = df[['warnings', 'openfda.product_type']] # filter for the columns of interest 
df['warnings'] = df['warnings'].apply(lambda x: ' '.join(eval(x))) # transform warnings from list of strings to single string
df['openfda.product_type'] = df['openfda.product_type'].apply(lambda x: eval(x)[0]) # transform product type from list to single string
df.rename(columns={'openfda.product_type': 'product_type'}, inplace=True) # rename product_type column 
df.to_csv('data/raw/drugs.csv', index=False) # save the dataframe as a csv to the data/raw directory