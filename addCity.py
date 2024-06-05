import requests
import json
from tqdm import tqdm

with open('cities.json', 'r') as f:
    cities_data = json.load(f)

url = 'http://0.0.0.0:5000/v2/cities'

total_cities = len(cities_data)
counter = 0

for city in tqdm(cities_data, desc="Sending requests", total=total_cities):
    json_data = {
        "id": city["id"],
        "name": city["name"],
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "postal_code": city["postal_code"],
        "state_id": city["state_id"]
    }

    response = requests.post(url, json=json_data)

    if response.status_code == 200:
        counter += 1
    else:
        print(f"Failed to add city {city['name']}. Error: {response.text}")

print(f"Processed {counter}/{total_cities} cities.")
