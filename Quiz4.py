#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:03:56 2021

@author: kyliewise
"""

# install neccessary packages
# pip install requests

########### ONLY RUN ONCE #######################
import json
import requests
import time
from csv import writer
import pandas as pd 

# create empy csv to store market data
df = pd.DataFrame(list())
df.to_csv('empty_csv.csv')

#1 Grab a list of quotes to get form Yahoo

apikey='AHn0QP9yk93DD8zblL0YA2PP4VjzOdyYF9ttoqi9'


url = "https://yfapi.net/v6/finance/quote"


############## CAN RE-RUN  #################

# Replace AAPL with ticker of choice 
querystring = {"symbols":"AAPL"}
headers = {
  'x-api-key': apikey
   }

# pulls ticker information from Yahoo Finance
response = requests.request("GET", url, headers=headers, params=querystring)

response.raise_for_status()  # raises exception when not a 2xx response

#if response.status_code != 204:
stock_json = response.json()

# converting markettime into standard format of time 
markettime = stock_json['quoteResponse']['result'][0]["regularMarketTime"]
market_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(markettime)))

# pull shortname, market time and market price as a string
data = str(stock_json['quoteResponse']['result'][0]["shortName"])  + ', ' + market_time + ', '+ str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"])


# Creates a function that will append data to csv as a new row 
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow([list_of_elem])

# append ticker information as new row 
append_list_as_row('empty_csv.csv', data)

