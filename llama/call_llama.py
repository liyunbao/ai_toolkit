import requests

# Settings
endpoint = "http://localhost:11434/api/generate"
model_name = "llama3.2:latest"  # or whatever model you pulled
prompt = "What is the Tableau Table Calculation?"

# Prepare the payload
payload = {
    "model": model_name,
    "prompt": prompt,
    "stream": False  # Set to False to get the full output at once
}

try:
    # Send the request
    response = requests.post(endpoint, json=payload)
    response.raise_for_status()  # Raise an error if not a 200 response
    data = response.json()

    # Print the result
    print("Response:")
    print(data.get("response", "No content returned."))

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
