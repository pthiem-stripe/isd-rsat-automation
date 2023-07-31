from autohubble import hubble_query_to_df, PRESTO
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
    logging.info(dist["distribution"])
    # Converting Hubble query to .csv
    df = hubble_query_to_df(dist["query"], PRESTO, force_refresh=True)
    logging.info(df)
    # TODO: Specify encoding format
    csv_file = DataFrame.to_csv(df, index=False)
    #f = open("a.csv", "a")
    #f.write(csv_file)
    #f.close()

    logging.info(csv_file)

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