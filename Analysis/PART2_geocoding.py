"""
Dissertation Title:
Impact of AirBnB on the Prices of Houses in Dublin between June 2021 and May 2022

- Student Name: Karina Jonina
- Student Code: c00278440
- Module Title: Dissertation
- Module Code: DISSC5201
- Supervisor: Dr Oisin Cawley
- Course Name: Master of Science in df Science
- Course Code: CW_KCDAR_M
- Assignment Weighting: 100%
- Due Date: 15th August 2022

Aim of this file:
Python script for batch geocoding of addresses using the Google Geocoding API.

This script allows for massive lists of addresses to be geocoded for free by pausing when the 
geocoder hits the free rate limit set by Google (2500 per day).  If you have an API key for paid
geocoding from Google, set it in the API key section.

Addresses for geocoding can be specified in a list of strings "addresses". In this script, addresses
come from a csv file with a column "Address". Adjust the code to your own requirements as needed.

After every 500 successul geocode operations, a temporary file with results is recorded in case of 
script failure / loss of connection later.
"""

import pandas as pd
import requests
import logging
import time

logger = logging.getLogger("root")
logger.setLevel(logging.DEBUG)
# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

# =============================================================================
# Configuration
# =============================================================================

# Setting the Google API key here. 
# Even if using the free 2500 queries a day, its worth getting an API key since the rate limit is 50 / second.
# With API_KEY = None,  an issue will occur 2 second delay every 10 requests or so

# With a "Google Maps Geocoding API" key from https://console.developers.google.com/apis/, 
# the daily limit will be 2500, but at a much faster rate.

# kjonina
# API_KEY = 'AIzaSyAorhx4hccWxNGZwgGK161AR1A-0yCZ9tA'

# # karinajonina
API_KEY = 'AIzaSyCvNQwTTAmxWeDUX4FSPk2Ztnb6xyf4iZw'
# 

# # joninakarina
# API_KEY = ''

# # liamcrehan
# API_KEY = ''

# Backoff time sets how many minutes to wait between google pings when your API limit is hit
BACKOFF_TIME = 30

# Setting output file name 
output_filename = 'Data/Geolocation/geocoding_ppr.csv'
# output_filename = 'Data/geocoding_ppr.csv'

# Return Full Google Results? If True, full JSON results from Google are included in output
RETURN_FULL_RESULTS = False

# =============================================================================
# Importing data
# =============================================================================
# Importing the df to a Pandas Dataframe
df = pd.read_csv("Data/clean_gda_ppr.csv")
# =============================================================================
# Selecting the relevant data
# =============================================================================
# print(df.head())
print('Number of Addresses in Greater Dublin Area sold between 1st July 2021 and 30 July 2022: ', df['total_address'].count())


# # =============================================================================
# # Save the dataset
# # =============================================================================
# # df.to_csv('data/clean_gba_ppr.csv', index=False)

# =============================================================================
# Adress - List creation        
# =============================================================================
# Forming a list of addresses for geocoding:
# Making a big list of all of the addresses to be processed.
addresses = list(df["total_address"].unique())

# print(addresses)

# =============================================================================
# Running Geocoding function 
# Ran over a number of days
# =============================================================================


test = addresses[:10]

# part_1 = addresses[:2500]
# print(len(part_1))


# part_2 = addresses[2500:5000]
# print(len(part_2))


# part_3 = addresses[5000:7500]
# print(len(part_3))


# part_4 = addresses[7500:10000]
# print(len(part_4))


# part_5 = addresses[10000:12500]
# print(len(part_5))


# part_6 = addresses[12500:15000]
# print(len(part_6))


# part_7 = addresses[15000:17500]
# print(len(part_7))


# part_8 = addresses[17500:20000]
# print(len(part_8))


# part_9 = addresses[20000:22500]
# print(len(part_9))


# part_10 = addresses[22500:25000]
# print(len(part_10))

# =============================================================================
# Geocoding Function Creation
# =============================================================================

def get_google_results(address, api_key=None, return_full_response=False):
    """
    Get geocode results from Google Maps Geocoding API.
    
    Note, that in the case of multiple google geocode reuslts, this function returns details of the FIRST result.
    
    @param address: String address as accurate as possible. For Example "18 Grafton Street, Dublin, Ireland"
    @param api_key: String API key if present from google. 
                    If supplied, requests will use your allowance from the Google API. If not, you
                    will be limited to the free usage of 2500 requests per day.
    @param return_full_response: Boolean to indicate if you'd like to return the full response from google. This
                    is useful if you'd like additional location details for storage or parsing later.
    """
    # Set up your Geocoding url
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address={}".format(address)
    if api_key is not None:
        geocode_url = geocode_url + "&key={}".format(api_key)
        
    # Ping google for the reuslts:
    results = requests.get(geocode_url)
    
    # Results will be in JSON format - convert to dict using requests functionality
    results = results.json()
    
    # if there's no results or an error, return empty results.
    if len(results['results']) == 0:
        output = {
            "formatted_address" : None,
            "latitude": None,
            "longitude": None,
            "accuracy": None,
            "google_place_id": None,
            "type": None,
            "postcode": None
        }
    else:    
        answer = results['results'][0]
        output = {
            "formatted_address" : answer.get('formatted_address'),
            "latitude": answer.get('geometry').get('location').get('lat'),
            "longitude": answer.get('geometry').get('location').get('lng'),
            "accuracy": answer.get('geometry').get('location_type'),
            "google_place_id": answer.get("place_id"),
            "type": ",".join(answer.get('types')),
            "postcode": ",".join([x['long_name'] for x in answer.get('address_components') 
                                  if 'postal_code' in x.get('types')])
        }
        
    # Append some other details:    
    output['input_string'] = address
    output['number_of_results'] = len(results['results'])
    output['status'] = results.get('status')
    if return_full_response is True:
        output['response'] = results
    
    return output

# =============================================================================
# PROCESSING LOOP 
# =============================================================================
# Checking that the API key is ok/valid, and internet access is ok
test_result = get_google_results("Clonakilty, Ireland", API_KEY, RETURN_FULL_RESULTS)
if (test_result['status'] != 'OK'): #or (test_result['total_address'] != 'London, UK'):
    logger.warning("There was an error when testing the Google Geocoder.")
    raise ConnectionError('Problem with test results from Google Geocode - check your API key and internet connection.')

# Create a list to hold results
results = []
# Go through each address in turn
for address in test:
    # While the address geocoding is not finished:
    geocoded = False
    while geocoded is not True:
        # Geocode the address with google
        try:
            geocode_result = get_google_results(address, API_KEY, return_full_response=RETURN_FULL_RESULTS)
        except Exception as e:
            logger.exception(e)
            logger.error("Major error with {}".format(address))
            logger.error("Skipping!")
            geocoded = True
            
        # If we're over the API limit, backoff for a while and try again later.
        if geocode_result['status'] == 'OVER_QUERY_LIMIT':
            logger.info("Hit Query Limit! Backing off for a bit.")
            time.sleep(BACKOFF_TIME * 60) # sleep for 30 minutes
            geocoded = False
        else:
            # If we're ok with API use, save the results
            # Note that the results might be empty / non-ok - log this
            if geocode_result['status'] != 'OK':
                logger.warning("Error geocoding {}: {}".format(address, geocode_result['status']))
            logger.debug("Geocoded: {}: {}".format(address, geocode_result['status']))
            results.append(geocode_result)           
            geocoded = True

    # Print status every 100 test
    if len(results) % 100 == 0:
     	logger.info("Completed {} of {} address".format(len(results), len(test)))
            
    # Every 500 test, save progress to file(in case of a failure so you have something!)
    if len(results) % 500 == 0:
        pd.DataFrame(results).to_csv("{}_bak".format(output_filename))

# All done
logger.info("Finished geocoding all addresses")

# =============================================================================
# Save the results to a CSV
# =============================================================================
# Write the full results to csv using the pandas library.
pd.DataFrame(results).to_csv('Data/Geolocation/geocoding_ppr_part_1.csv')

# pd.DataFrame(results).to_csv('Data/Geolocation/geocoding_ppr_test.csv')