# INF601 - Advanced Programming in Python
# Clayton Allen
# Mini Project 1

"""
This script makes use of a REST API available through rapidapi.com. 
Please visit the provided link to explore additional endpoints.
https://rapidapi.com/asepscareer/api/yfinance-stock-market-data/
"""

#The required libraries and modules for this project to work. List of all dependencies will be shown in the "Requirements.txt" text file.


import os # Required to make the directory "Images" which is used as a staging area for outputted image files. 
import requests  # Required to send API requests to endpoints
import matplotlib.pyplot as plt # This is used to output data from API responses to scatterplot PNG files. 
from config import * # This imports everything located in the "Config.py" file, which is used as a placeholder for your API key. 
from datetime import datetime   # Used to convert epoch time to standard datetime. 
import numpy as np  # Used to convert the list of data into a numpy array, later to be used as input data for the scatterplot images.
import time  # Import the time module

# Function used to get stock data over the past 10 days for a given stock symbol.
def get_trades(apikey, symbol): #Positional arguments used as input for funciton. 
    url = "https://yfinance-stock-market-data.p.rapidapi.com/price"

    # Feel free to modify the day count. 
    payload = {
        "period": "10d",
        "symbol": symbol
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": apikey,
        "X-RapidAPI-Host": "yfinance-stock-market-data.p.rapidapi.com"
    }

    # Adjust this as needed. RapidAPI "yFinance" only allows for one query per second for free users. You can reduce this wait value by giving the yfinance overlords more money.  

    time.sleep(1)

    response = requests.post(url, data=payload, headers=headers)
    
    # Error checking to ensure request is accepted before showing output. Returns an error code if nothing is shown. 
    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        print(f"Error: {response.status_code}")
        return None
    
    # List of symbols for the companies that I've invested in the past.
companies = ["AAPL", "GE", "NET", "NVDA", "RTX"]

# Create the 'charts' directory if it doesn't exist. This will be used to store the five scatterplot .PNG files.
output_directory = 'charts'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for symbol in companies:
    data = get_trades(apikey=X_RapidAPI_Key, symbol=symbol)