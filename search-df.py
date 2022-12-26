import json
import pandas
import requests
from keyfile import serpkey

fptr = open("search0.json", 'r')

results = json.load(fptr)

fptr.close()

s = []
for result in results['organic_results'][0:1]:
    d = {}
    d['title']   = result['title']
    d['link']    = result['link']
    d['snippet'] = result['snippet']
    serplink     = result['inline_links']['serpapi_cite_link']
    cite         = requests.get(serplink, params={'api_key': serpkey})
    d['cite']        = cite.json()
    d['serplink']    = serplink
    s.append(pandas.Series(d))

df = pandas.DataFrame(s)

fptr = open('pub.csv', 'w')

df.to_csv(fptr)

fptr.close()



