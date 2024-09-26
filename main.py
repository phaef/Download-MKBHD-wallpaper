import os
import json
import requests

# URL to download the JSON file
json_url = "https://storage.googleapis.com/panels-api/data/20240916/media-1a-i-p~s"

# Step 1: Download the JSON file
json_response = requests.get(json_url)
if json_response.status_code != 200:
    raise Exception(f"Failed to download JSON: Status code {json_response.status_code}")
json_data = json_response.json()

# Step 2: Create output directory
output_dir = "downloaded_files"
os.makedirs(output_dir, exist_ok=True)

# Step 3: Iterate over the JSON and download files with "dhd" keys
for key, value in json_data.get("data", {}).items():
    if "dhd" in value:
        file_url = value["dhd"]
        file_name = os.path.join(output_dir, f"{key}.jpg")
        try:
            print(f"Downloading {file_url} to {file_name}")
            response = requests.get(file_url)
            response.raise_for_status()  # Check if the request was successful
            with open(file_name, "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {file_name}")
        except Exception as e:
            print(f"Failed to download {file_url}: {e}")
