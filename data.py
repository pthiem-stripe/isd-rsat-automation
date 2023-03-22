from dotenv import load_dotenv
import pandas as pd
import os
import requests
import json

load_dotenv()

# Qualtrics credentials
QUALTRICS_ENDPOINT = "https://ca1.qualtrics.com/API/v3/distributions/"
QUALTRICS_API_TOKEN = os.getenv('QUALTRICS_API_TOKEN')
HEADERS = {
    "X-API-TOKEN": QUALTRICS_API_TOKEN,
}

# Survey IDs
SURVEYS = ["SV_eeqjEriQPnotbPE", "SV_bejhQjWf2dfoJVk"]

data_df = pd.DataFrame()
for survey in SURVEYS:
    params = {
        "surveyId": survey
    }

    response = requests.get(url=QUALTRICS_ENDPOINT,
                            params=params, headers=HEADERS)
    data_json = response.json()

    elements = data_json["result"]["elements"]
    survey_df = pd.json_normalize(elements)
    data_df = pd.concat([data_df, survey_df])

data_df.to_csv('qualtrics_data.csv')
