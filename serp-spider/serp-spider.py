#spider using Serp API.
import requests
import json
from keyfile import serp_key as key
from serpapi import GoogleScholarSearch

search_params = {'api_key': key}
results = []
GoogleScholarSearch.SERP_API_KEY = key
search = GoogleScholarSearch({"q": "netpyne", "num": 20, "as_vis": 1, "as_ylo": 2021}).get_json()
results.append(search)
other_pages = search['serpapi_pagination']['other_pages']

for page in other_pages:
    serp_link = other_pages[page]
    search = requests.get(serp_link, params=search_params).json()
    results.append(search)

for i, result in enumerate(results):
    fptr = open("search%s.json" %(i), "w")
    json.dump(result, fptr)
    fptr.close()
