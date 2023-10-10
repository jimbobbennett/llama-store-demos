"""
This calls the /user endpoint on the llama store API to create a user.
"""
import json
import requests

# The URL of the llama store API
BASE_URL = "http://localhost:8000/"

# Build the new user as a JSON object
new_user = {
    "email": "llama@liblab.com",
    "password": "Llama123!",
}

# Send the post request
user_response = requests.post(BASE_URL + "user", json=new_user, timeout=5)

# Show the response
print(f"Response status code: {user_response.status_code}")
print(json.dumps(user_response.json(), indent=2))
