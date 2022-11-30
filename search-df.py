import json
import pandas as pd

#final note, beatifulsoup4 >> serpapi. will use bs4
fptr = open("search0.json", 'r')
results = json.load(fptr)

df = []
for result in results['organic_results']:
    d = {}
    d['title']   = result['title']
    d['link']    = result['link']
    d['snippet'] = result['snippet']
    pubinfo      = result['publication_info']['summary']
