# isd-rsat-automation
Scripts to automate sending RSAT emails and reading results for ISD through Qualtrics.

## How to send RSATs
run
```python qualtrics.py```

## qualtrics.py
This script loops through every distribution (defined in `distribution.json`), queries data from hubble, converts it into a csv file and uploads it to Qualtrics. Qualtrics then runs the defined automations to send out the surveys.

## distributions.json
A distribution object is defined for every survey that needs to be sent. Each distribution has a corresponding hubble query, a survey ID and an automation endpoint. The automation endpoint is used to upload csv files with contact data.

### Go Live / End of engagement
The script sends out the same RSAT survey twice. Once a user went live, and another time when the end of engagement date has been hit.
