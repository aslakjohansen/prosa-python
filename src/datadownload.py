#!/usr/bin/env python3

import requests

url = "https://data.un.org/_Docs/SYB/CSV/SYB68_1_202511_Population,%20Surface%20Area%20and%20Density.csv"

filename = "popdata.csv"

response = requests.get(url)

if response.status_code == 200:
  with open(filename, "w") as fo:
    fo.writelines([response.text])
else:
  print("Oops, something went wrong ...")
