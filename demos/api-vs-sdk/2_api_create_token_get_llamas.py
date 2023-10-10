"""
This calls the /token endpoint on the llama store API to create an API token.
It then uses this to get the llamas
"""
import json
import requests

# The URL of the llama store API
BASE_URL = "http://localhost:8000/"

# Build the token request as a JSON object
token_request = {
    "email": "llama@liblab.com",
    "password": "Llama123!",
}

# Send the post request
token_response = requests.post(BASE_URL + "token", json=token_request, timeout=5)
token_response_json = token_response.json()

# Show the response
print(f"Response status code: {token_response.status_code}")
print(json.dumps(token_response_json, indent=2))

# Get the token from the response
token = token_response_json["access_token"]
headers = {"Authorization": f"Bearer {token}"}

# Get the llamas
llamas_response = requests.get(BASE_URL + "llama", timeout=5, headers=headers)
print(f"Response status code: {llamas_response.status_code}")
print(json.dumps(llamas_response.json(), indent=2))

# Get one llama
llama_response = requests.get(BASE_URL + "llama/1", timeout=5, headers=headers)
print(f"Response status code: {llama_response.status_code}")
print(json.dumps(llama_response.json(), indent=2))
