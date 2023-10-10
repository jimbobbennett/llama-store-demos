# API vs SDK demos

This folder container a set of demos comparing the developer experience of accessing the llama store using its API, vs using the generated SDK from liblab.

| File                                                                                     | Description |
| ---------------------------------------------------------------------------------------- | ----------- |
| [`1_api_create_user.py`](1_api_create_user.py)                                           | Create a user using the API (code is intentionally wrong to illustrate lack of type safety) |
| [`2_api_create_token_get_llamas.py`](2_api_create_token_get_llamas.py)                   | This assumes the previous script has been run correctly to create a user. It generates an API token for that user and lists the llamas. The token is not set in the header to show the benefit of an SDK to always set the token. |
| [`3_sdk_create_user_get_token_and_llamas.py`](3_sdk_create_user_get_token_and_llamas.py) | This script uses the SDK. It is basically empty and should be used to create a user, get the token, set it on the API, and get the llamas tp show type safety. |

The [`final`](final) folder contains the final version of the scripts, with the API and SDK versions and the complete code that works.

To run the final versions, run them all in order. They assume the demo versions have not been run. You also cannot run the user create script more than once, as the user will already exist. You either need to update the email, or re-create the database.

To re-create the database, stop the API, then run the following command:

```bash
cd llama-store
./scripts/recreate_database.sh
```

Then restart the API.
