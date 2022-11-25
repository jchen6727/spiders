#spider using Serp API.
import requests
try:
    from keyfile import serpkey
except:
    print("missing serp API key")
from serpapi import GoogleScholarSearch

GoogleScholarSearch.SERP_API_KEY = serpkey
search = GoogleScholarSearch({"q": "netpyne", "num": 20, "as_vis": 1, "as_ylo": 2021})
results = search.get_dict()
entries = results['organic_results']
pubdata = []

for entry in entries:
    d = {}
    d['title'] = entry['title']
    d['snippet'] = entry['snippet']
    #resources = entry['resources']
    clink = entry['inline_links']['serpapi_cite_link']
    rcite = requests.get(clink, params={'api_key': serpkey}) #HIGH COST REQUEST
    d['cite'] = rcite.json()
    d['all'] = entry
    pubdata.append(d)