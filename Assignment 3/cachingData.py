'''
@Author: Nishith Kumar
@brief: The script caches csv from metadata's download urls in case of network failure
@note: The script is not used in the project, but given the api is not stable, it is a good practice to cache the data
@usage: python cachingData.py
@output: csv files in the same directory
@dependency: pandas, requests, os
@see:
@todo:
@bug:
@warning:
'''

import requests
import metadata.txt as dataInfo
import pandas as pd
import os

# Define the URLs
max_data_url = dataInfo["distribution"][0]["downloadURL"]
min_data_url = dataInfo["distribution"][1]["downloadURL"]

# Define the local file paths for caching
max_cache_file = "max_data.csv"
min_cache_file = "min_data.csv"

# Check if the local cache files exist
if os.path.exists(max_cache_file) and os.path.exists(min_cache_file):
    # If the cache files exist, load data from them
    df_max = pd.read_csv(max_cache_file)
    df_min = pd.read_csv(min_cache_file)
else:
    # If cache files don't exist, download the data and save it to cache
    df_max = pd.read_csv(max_data_url)
    df_min = pd.read_csv(min_data_url)
    
    # Save the DataFrames to cache files
    df_max.to_csv(max_cache_file, index=False)
    df_min.to_csv(min_cache_file, index=False)

# Now, you can use df_max and df_min, which will be loaded from cache if available or downloaded if not.
