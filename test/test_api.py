#!/usr/bin/env python

import ast
import json
import os
import pprint
import requests
import sys

try:
    os.environ['IP_ADDR']
    os.environ['PORT']
except:
    print("Please export IP_ADDR and PORT of modify this file with the vars")
    sys.exit(1)

IP_ADDR=os.environ.get('IP_ADDR')
PORT=os.environ.get('PORT')

pp = pprint.PrettyPrinter(indent=4)

SCORING_URL = "http://" + IP_ADDR + ":" + PORT + "/v1/deployments/circle/online"

payload = {'values': [[10], [20]], 'fields': ['radius']}
header = {'Content-Type':'application/json'}

r = requests.post(SCORING_URL, json=payload, headers=header)

print(str(r.text))
