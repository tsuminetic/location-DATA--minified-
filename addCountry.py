import requests
import json
from tqdm import tqdm

with open('countries.json', 'r') as f:
    countries_data = json.load(f)

url = 'http://0.0.0.0:5000/v2/countries'

total_countries = len(countries_data)
counter = 0

for country in tqdm(countries_data, desc="Sending requests", total=total_countries):
    json_data = {
        "id": country["id"],
        "name": country["name"],
        "capital": country["capital"],
        "population": country["population"],
        "currency": country["currency"],
        "official_language": country["official_language"],
        "continent": country["continent"],
        "iso_code": country["iso_code"],
        "calling_code": country["calling_code"],
        "timezone": country["timezone"]
    }

    response = requests.post(url, json=json_data)

    if response.status_code == 200:
        counter += 1
    else:
        print(f"Failed to add country {country['name']}. Error: {response.text}")

print(f"Processed {counter}/{total_countries} countries.")
