import requests
body = {
    "email": "test_email@gmail.com",
    "name": 'James Testerton'
}

response = requests.post('https://scribedata.app/request_api_key', json=body)
response_json = response.json()

print(response_json)