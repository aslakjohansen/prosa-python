#!/usr/bin/env python

from sys import exit
import requests
import re
import json

pattern_continent = re.compile("^<h2 id=\"([^\"]+)\">")
pattern_country   = re.compile("^wiki/Flag_of_([^\"]+)\"")

# make wikipedia robot policy happy:
headers = {
  "User-Agent": "Demo for python requests module https://python.asjo.dk"
}

url = "https://simple.wikipedia.org/wiki/List_of_countries_by_continents"
response = requests.get(url, headers=headers)

if not response.status_code==200:
  print("Error fetching url: "+response.text)
print("Downloaded. Processing will take some time (90s on my machine) ...")

# process
contents = response.text
continent = None
mapping = {}
while len(contents)>0:
  mo_continent = pattern_continent.match(contents)
  mo_country = pattern_country.match(contents)
  
  if mo_continent:
    continent = mo_continent.group(1).replace("_", " ")
    contents = contents[len(mo_continent.group(0)):]
  if mo_country:
    country = mo_country.group(1).replace("_", " ").lower()
    if not "&quot" in country:
      mapping[country] = continent
    contents = contents[len(mo_country.group(0)):]
  else:
    contents = contents[1:]

# store
s = json.dumps(mapping, sort_keys=True, indent=4, separators=(',', ': '))
with open("country2continent.json", "w") as fo:
  fo.writelines([s])

