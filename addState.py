import requests
import json
from tqdm import tqdm

with open('states.json', 'r') as f:
    states_data = json.load(f)

url = 'http://0.0.0.0:5000/v2/states'

total_states = len(states_data)
counter = 0

for state in tqdm(states_data, desc="Sending requests", total=total_states):
    json_data = {
        "id": state["id"],
        "name": state["name"],
        "latitude": state["latitude"],
        "longitude": state["longitude"],
        "population": state["population"],
        "timezone": state["timezone"],
        "country_id": state["country_id"]
    }

    response = requests.post(url, json=json_data)

    if response.status_code == 200:
        counter += 1
    else:
        print(f"Failed to add state {state['name']}. Error: {response.text}")

print(f"Processed {counter}/{total_states} states.")
