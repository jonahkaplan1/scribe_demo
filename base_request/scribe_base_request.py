# Import The Two Libraries We Need
import requests
import json

# Read in Your SQL File For The Request
with open('Downloads/my_query.sql', 'r') as file:
    sql_file = file.read()

body = {
    "sql_contents": sql_file,
    "scribe_api_key": 'my_api_key', # Replace this with your API Key
    "tenancy": "prod",
    "produce_scribe_json_response": True
}

response = requests.post('https://scribedata.app/scribe', json=body)
response_json = response.json()

with open('scribe_response.json', 'w') as outfile:
    json.dump(response_json, outfile)
