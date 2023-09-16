# miniproject1CA

INF601 Advanced Programming with Python

Clayton Allen

## Description

This project utilizies several third party libraries to send API requests using hardcoded stock symbols using the yfinance API endpoint. The date and close values are parsed and used as input for lists. The lists are converted to numpy arrays which are then used as input for matplotlib methods. The methods are used to create scatterplots for 5 stock symbol closing prices throughout the course of 10 days. Scatterplot PNG files are stored as output to a directory titled "charts". If the folder doesn't exist, the directory will be created relative to where the command was run. 

## Pip install instructions

Please run the following:

```
pip install requirements.txt
```

## How to run
In a terminal, please type the following:

```
**python main.py**
```