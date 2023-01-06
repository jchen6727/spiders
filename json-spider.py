"""
use with json files produced by serp-spider.py to grab relevant citation data
"""

import json
import pandas
import requests
from keyfile import serp_key as key

search_params = {'api_key': key}

def json_to_csv( filename = "search0"):
    fptr = open("%s.json" %(filename), "r")
    results = json.load(fptr)
    fptr.close()
    s = []
    for result in results['organic_results']:
        serplink = result['inline_links']['serpapi_cite_link']
        cite = requests.get(serplink, params=search_params).json()
        try:
            citel = cite['citations'][4]['snippet'].split('.') #not all journals have vancouver citation
        except:
            citel = cite['citations'][0]['snippet'].
        s.append(
            pandas.Series(
                {'Title': result['title'],
                 'Link': result['link'],
                 'Snippet': result['snippet'],
                 'cite': cite,
                 'Authors': citel[0],
                 'Journal': citel[2],
                 'Year': citel[3],
                 'serplink': serplink}
            )
        )
    df = pandas.DataFrame(s)
    fptr = open("%s.csv" %(filename), 'w')
    df.to_csv(fptr)
    fptr.close()
    return df

files = [
    "search0",
    "search1",
    "search2",
    "search3",
]

dfs = []

for file in files:
    dfs.append(json_to_csv(file))

df = pandas.concat(dfs)

fptr = open("all.csv", 'w')
df.to_csv(fptr)
fptr.close()