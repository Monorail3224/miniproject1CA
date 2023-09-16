# INF601 - Advanced Programming in Python
# Clayton Allen
# Mini Project 1

"""
This script makes use of a REST API available through rapidapi.com. 
Please visit the provided link to explore additional endpoints.
https://rapidapi.com/asepscareer/api/yfinance-stock-market-data/
"""

    # Grading criteria copied from blackboard. 

'''
    (5/5 points) Initial comments with your name, class and project at the top of your .py file.
    (5/5 points) Proper import of packages used.
    (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
    (10/10 points) Store this information in a list that you will convert to a array in NumPy.
    (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
    (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
    (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
    (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
    (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.
'''

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

    if data is not None:
        # Extract the close values and dates from the API response and save them to lists
        close_prices = [entry['Close'] for entry in data]
        # Convert Epoch time to standard datetime and save to a list
        dates = [datetime.utcfromtimestamp(entry['Date'] / 1000).strftime('%Y-%m-%d') for entry in data]

        # Convert the lists to NumPy ndarrays
        close_prices_array = np.array(close_prices)
        dates_array = np.array(dates)

        # The creation of this directory is relative to the path in which the python script is run from.
        # Define the file path where you want to save the image for each company and append "_close_prices.png" to the end of the stock symbol
        file_path = os.path.join(output_directory, f'{symbol.lower()}_close_prices.png')

        
        # Create a scatterplot using Matplotlib
        plt.figure(figsize=(10, 10), facecolor='beige')  # Adjust the width and height of the scatterplot image in and set the background color 
        plt.scatter(dates_array, close_prices_array, marker='H', color='green', label=f'{symbol} Close Prices')
        plt.xlabel('Date')
        plt.ylabel('Closing Price in Dollar Amount')
        plt.title(f'{symbol} Stock Close Prices Over the Past 10 Days', fontsize=18)
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)

        # Save the scatterplot image to the specified file path
        plt.savefig(file_path)

        # Close the Matplotlib plot to avoid displaying it
        plt.close()

        print(f"Image saved to {file_path}")
