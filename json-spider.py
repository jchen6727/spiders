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
        cite = requests.get(serplink, params=search_params).to_dict()
        s.append(
            pandas.Series(
                {'title': result['title'],
                 'link': result['link'],
                 'snippet': result['snippet'],
                 'cite': cite,
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

