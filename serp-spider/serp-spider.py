#spider using Serp API.
import requests
import json
import argparse

from serpapi import GoogleScholarSearch
import pandas

parse = argparse.ArgumentParser()
parse.add_argument("-k" "--key", help="file containing the api key (from https://serpapi.com/dashboard#)", default="serpapi.key", type=str)
parse.add_argument("-q", "--query", help="querystring to search for", default="netpyne", type=str)
parse.add_argument("-y", "--ylo", help="only results from year > ylo", default=2020, type=int)
parse.add_argument("-o", "--output", help="output file", default="search", type=str)
parse.add_argument("-n", "--num", help="number of API calls", default=20, type=int)

def get_key(keyfile="serpapi.key"):
    """
    get api key from file
    :param keyfile:
    :return key:
    """
    with open(keyfile, "r") as fptr:
        key = fptr.readline().strip()
    #fptr.close() # with statement closes file
    return key
def get_outer(key, query="netpyne", ylo=2020, numq=100):
    """
    get outer search results from Serp API
    :param key: api key
    :param query: querystring
    :param ylo: only results from year > ylo
    :param output: output file
    :param num: number of queries to return
    :return results: json results
    """
    GoogleScholarSearch.SERP_API_KEY = key
    search_params = {'api_key': key}
    search = GoogleScholarSearch({"q": query, "num": 20, "as_vis": 1, "as_ylo": ylo}).get_json()
    results = []
    results.append(search)
    other_pages = search['serpapi_pagination']['other_pages'] # 'other_pages' is a list of
    numq = numq - 1
    for page, serp_link in tuple(other_pages.items())[:numq]:
        search = requests.get(serp_link, params=search_params).json()
        results.append(search)
    return results

def collate_organic(results, output="search.csv"):
    """
    collate organic results from outer search results
    :param results:
    :return organic_results:
    """
    organic_results = [pandas.json_normalize(result['organic_results']) for result in results]
    organic_results = pandas.concat(organic_results, ignore_index=True)
    if output:
        with open(output, 'w') as fptr:
            organic_results.to_csv(fptr)
    return organic_results

def get_inner(results, key, numq = 100):
    """
    use outer results to generate tabulated citation data (parsed with vancouver citation)
    N.B. each inner result is a separate API call...
    #TODO itterrows used for testing, switch to better method when completed
    :param results:
    :param key:
    :return df:
    """
    search_params = {'api_key': key}
    s = []
    for row, result in results[:numq].iterrows():
        serplink = result['inline_links.serpapi_cite_link']
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
    return df
