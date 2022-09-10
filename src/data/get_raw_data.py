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
            return get_all_drugs(url, all_drugs)
        else: # the last page of results does not include a Link in the header 
            return all_drugs

url = 'https://api.fda.gov/drug/label.json?search=_exists_:warnings+AND+_exists_:openfda.product_type&limit=1000'
all_drugs = get_all_drugs(url)
df = pd.json_normalize(all_drugs) 
df.to_csv('data/raw/drugs.csv', index=False)