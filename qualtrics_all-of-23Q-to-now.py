from autohubble import hubble_permalink_to_df
from pandas import DataFrame
from dotenv import load_dotenv
import os
import requests
import logging
import json

load_dotenv()

# Qualtrics credentials
QUALTRICS_ENDPOINT = "https://iad1.qualtrics.com/automations-file-service/automations/"
QUALTRICS_API_TOKEN = os.getenv('QUALTRICS_API_TOKEN')
HEADERS = {
    "X-API-TOKEN": QUALTRICS_API_TOKEN,
}


FILE = open("./distributions.json")
DISTRIBUTIONS = json.load(FILE)

# Logger
logging.basicConfig(filename="qualtrics_upload_log_one-off.txt",
                    format="%(asctime)s %(levelname)-8s %(message)s",
                    encoding="utf-8", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")

        



logging.info("https://hubble.corp.stripe.com/queries/pthiem/228db8ea")
# Converting Hubble query to .csv
df = hubble_permalink_to_df("https://hubble.corp.stripe.com/queries/pthiem/228db8ea")
logging.info(df)
# TODO: Specify encoding format
csv_file = DataFrame.to_csv(df)

# Return error if file error
if not csv_file:
    logging.warning("No csv file to upload")

# Qualtrics API request
dist_url = QUALTRICS_ENDPOINT + "AU_7WEZufaraVR6WMa/files"
params = {
    "file": csv_file
}

logging.info("Qualtrics upload disabled")

#Log response
#response = requests.post(url=dist_url, files=params, headers=HEADERS)
#logging.info(response.text)

# Problem with permalinks is if you need to update them
# Better to have the query in a .sql file, and refer to that using the library

# If you are logged off, it won't run - machine always on
#
