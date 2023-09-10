# INF601 - Advanced Programming in Python
# Clayton Allen
# Mini Project 1

"""
This script makes use of a REST API available through rapidapi.com. 
Please visit the provided link to explore additional endpoints.
https://rapidapi.com/asepscareer/api/yfinance-stock-market-data/
"""

import requests
from config import *
import pprint

url = "https://yfinance-stock-market-data.p.rapidapi.com/price"

payload = {
	"period": "10d",
	"symbol": "AAPL"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": X_RapidAPI_Key, # Assigned variable in "config.py" that contains the API key
	"X-RapidAPI-Host": "yfinance-stock-market-data.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

pprint.pprint(response.json())
    