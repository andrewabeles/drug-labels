import requests
import re 
import pandas as pd

def get_all_drugs(url, all_drugs=[]):
    r = requests.get(url)
    if r.status_code == 200:
        drugs = r.json()['results']
        all_drugs.extend(drugs)
        if 'Link' in r.headers:
            url = re.findall(r'<(.*)>', r.headers['Link'])[0] # extract the next page's url from response header
            return get_all_drugs(url, all_drugs) # pass it through the function
        else: # the last page of results does not include a Link in the header 
            return all_drugs

url = 'https://api.fda.gov/drug/label.json?search=_exists_:warnings+AND+_exists_:openfda.product_type&limit=1000'
drugs = get_all_drugs(url)
drugs = drugs[['warnings', 'openfda.product_type']]
drugs['warnings'] = drugs['warnings'].apply(lambda x: ' '.join(eval(x))) # transform warnings from list of strings to single string
drugs['product_type'] = drugs['openfda.product_type'].apply(lambda x: eval(x)[0]) # transform product type from list to single string
drugs = drugs[['warnings', 'product_type']]
df = pd.json_normalize(drugs) 
df.to_csv('data/raw/drugs.csv', index=False)