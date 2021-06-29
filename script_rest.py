# Using script to update rest data
# dj30, sp500, divs, etf

import sys
import requests
import json


ticker = sys.argv[1]
ticker = str(ticker)

url = f"http://127.0.0.1:8000/update/{ticker}/"
payload = {"index": f"{ticker}"}
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)
print(ticker)
