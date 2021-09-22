# Import The Two Libraries We Need
import requests
import json

# Read in Your SQL File For The Request
with open('Downloads/my_query.sql', 'r') as file:
    sql_file = file.read()

# Our request body
body = {
    "sql_contents": sql_file,
    "scribe_api_key": 'my_api_key', # Replace this with your API Key
    "tenancy": "prod",
    "produce_scribe_json_response": False,
    "produce_html_documentation": True
}

# Make our request
response = requests.post('https://scribedata.app/scribe', json=body)
response_json = response.json()

print(response_json)


# The html documentation response object is a string of raw html.
# It can be written directly to an HMTL File
file_path = "Downloads/my_query_visualized.html"
text_file = open(file_path, "w")
n = text_file.write(response_json['html_documentation'])
text_file.close()
