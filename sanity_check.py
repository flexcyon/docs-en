#!/usr/bin/env python3.12

import requests
import json
import subprocess
import time
import re
import traceback

def sample_libretranslate_post():
    payload = {
        "q": "test\n",
        "source": "en",
        "target": "zh",
        "format": "text",
        "alternatives": 3,
        "api_key": ""
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Send the POST request
        response = requests.post(
            "http://127.0.0.1:5000/translate",
            headers=headers,
            json=payload,  # Use 'json' parameter to automatically serialize the dict to JSON
            timeout=60     # Add a timeout for robustness
        )

        # Raise an exception for HTTP errors (4xx or 5xx)
        response.raise_for_status()

        # Parse the JSON response
        response_data = response.json()

        # Print the response data
        print(json.dumps(response_data, indent=2)) # Pretty print the JSON

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response body: {e.response.text}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON response. Raw response: {response.text}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    sample_libretranslate_post()
