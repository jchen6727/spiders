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
            citev = cite['citations'][4]['snippet'].split('.') # vancouver citation TODO improve parsing
            assert(citev[3]) # break to except if vancouver citation missing (assert fails)
        except:
            print("missing appropriate citation: %s" %(result['title']))
            citev = ['NULL'] * 4
        s.append(
            pandas.Series(
                {'Title': result['title'],
                 'Link': result['link'],
                 'Snippet': result['snippet'],
                 'cite': cite,
                 'Authors': citev[0],
                 'Journal': citev[2],
                 'Year': citev[3],
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