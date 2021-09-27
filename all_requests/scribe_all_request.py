# Import The Two Libraries We Need
import requests
import json
import ruamel.yaml

# Read in Your SQL File For The Request
with open('Downloads/my_query.sql', 'r') as file:
    sql_file = file.read()

# Our request body
body = {
    "sql_contents": sql_file,
    "scribe_api_key": 'my_api_key', # Replace this with your API Key
    "tenancy": "prod",
    "produce_scribe_json_response": True, 
    "produce_html_documentation": True, 
    "produce_dbt_model_yml": True,
    "file_or_table_name": "my_query", # Optional, This sets the name of our dbt model name
    "dbt_model_yml_column_tests": 'both', # Optional, default is 'none'
    "dbt_model_yml_version": 2,  # Optional, default is 2
    "dbt_model_yml_table_description": "In this table we define our customer metrics" # Optional, default is an empty string
}

# Make our request
response = requests.post('https://scribedata.app/scribe', json=body)
response_json = response.json()

# save scribe response json
with open('scribe_response.json', 'w') as outfile:
    json.dump(response_json, outfile)


# The html documentation response object is a string of raw html.
# It can be written directly to an HMTL File
file_path = "Downloads/my_query_visualized.html"
text_file = open(file_path, "w") # Create the file in the path above
n = text_file.write(response_json['html_documentation']) # Write out HTML string directly to the new file
text_file.close()


# The dbt_model_yml response is a json structured yaml file.
# We use ruamel.yaml to format the results into a dbt accepted file
file_path = "Downloads/my_query_dbt_model.yml"
file = open(file_path, "w")
yaml = ruamel.yaml.YAML()
yaml.representer.ignore_aliases = lambda *data: True
yaml.indent(sequence=4, offset=2)
# This sets line width, so a long description doesnt create two lines (which would cause an error)
yaml.width = 4000
yaml.dump(response_json['dbt_model_yml'], file)
file.close()
