from dotenv import load_dotenv
import pandas as pd
import os
import requests
import json
import logging

load_dotenv()

# Qualtrics credentials
QUALTRICS_ENDPOINT = "https://ca1.qualtrics.com/API/v3/distributions/"
QUALTRICS_API_TOKEN = os.getenv('QUALTRICS_API_TOKEN')
HEADERS = {
    "X-API-TOKEN": QUALTRICS_API_TOKEN,
}

# Logger
logging.basicConfig(filename="qualtrics_download_log.txt",
                    format="%(asctime)s %(levelname)-8s %(message)s",
                    encoding="utf-8", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")

logging.info("start download")

data_df = pd.DataFrame()
params = {
    "surveyId": "SV_5bFlFw94TvTeurQ"
}

response = requests.get(url=QUALTRICS_ENDPOINT,
                        params=params, headers=HEADERS)

logging.info(response)
data_json = response.json()
elements = data_json["result"]["elements"]
survey_df = pd.json_normalize(elements)
logging.info(survey_df)
survey_df.to_csv('historic.csv')
