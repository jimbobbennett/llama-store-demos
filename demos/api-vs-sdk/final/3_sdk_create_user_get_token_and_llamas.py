"""
This uses the llama store SDK to:
- Create a user
- Get an API token
- Use the token to get llamas
- Use the token to get one llama
"""
from llamastore import Llamastore
from llamastore.models import ApiTokenRequest, UserRegistration

# Create the llama store client
llama_store = Llamastore()

# Create a user
user_registration = UserRegistration(email="sdk_llama@liblab.com", password="Llama123!")
user = llama_store.user.register_user(user_registration)
print(f"Created user: {user.email} with ID {user.id}")

# Get an API token
api_token_request = ApiTokenRequest(email=user_registration.email, password=user_registration.password)
token = llama_store.token.create_api_token(api_token_request)

# Set the API token on the llama store client
llama_store.set_access_token(token.access_token)

# Get the llamas
llamas = llama_store.llama.get_llamas()

for llama in llamas:
    print(f"Got llama: {llama.name}")

# Get one llama
llama = llama_store.llama.get_llama_by_id(1)
print(f"\nGot 1 llama: {llama.name}")