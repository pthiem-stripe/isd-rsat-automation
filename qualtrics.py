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
logging.basicConfig(filename="qualtrics_upload_log.txt",
                    format="%(asctime)s %(levelname)-8s %(message)s",
                    encoding="utf-8", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")


# Upload a file for each distribution
for dist in DISTRIBUTIONS:
    logging.info(dist["permalink"])
    # Converting Hubble query to .csv
    df = hubble_permalink_to_df(dist["permalink"])
    logging.info(df)
    # TODO: Specify encoding format
    csv_file = DataFrame.to_csv(df)

    # Return error if file error
    if not csv_file:
        logging.warning("No csv file to upload")

    # Qualtrics API request
    dist_url = QUALTRICS_ENDPOINT + dist["endpoint"]
    params = {
        "file": csv_file
    }

    #Log response
    response = requests.post(url=dist_url, files=params, headers=HEADERS)
    logging.info(response.text)

# Problem with permalinks is if you need to update them
# Better to have the query in a .sql file, and refer to that using the library

# If you are logged off, it won't run - machine always on
#
