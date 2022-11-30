from pubdata import data
import json
import pandas as pd


"""
csv stuff:
Title,Slug,Collection ID,Item ID,Created On,Updated On,Published On,Journal,Year,Authors,Link,Team Members
"""
s = []

for pub in data:
    d = {}
    raw = pub['cite']['citations'][4]['snippet']
    cite = pub['cite']['citations'][4]['snippet'].split('.')
    if len(cite) > 3:
        d['Title'] = pub['title']
        d['Authors'] = cite[0]
        d['Journal'] = cite[2]
        d['Year'] = cite[3]
        #d['snippet'] = pub['snippet']
        #d['raw'] = raw
        s.append(pd.Series(d))

df = pd.DataFrame(s)

fptr = open('pub.csv', 'w')
df.to_csv(fptr)
fptr.close()


