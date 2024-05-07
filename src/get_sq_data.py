import requests
import json


def query_api(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        # Process the data here
        print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

# Example usage
new_api_url = "https://artpal.ngrok.io/api/projects/license_usage"
response_data = query_api(new_api_url, headers={"Authorization": "Bearer squ_cefbc007eaa5a641017356b852f32598d0f6ec76"})
filename = new_api_url.split("/")[-2] + "-" + new_api_url.split("/")[-1] + ".json"
save_to_json(response_data, filename)

# Additional usage
new_api_url = "https://artpal.ngrok.io/api/qualitygates/list"
response_data = query_api(new_api_url, headers={"Authorization": "Bearer squ_cefbc007eaa5a641017356b852f32598d0f6ec76"})
filename = new_api_url.split("/")[-2] + "-" + new_api_url.split("/")[-1] + ".json"
save_to_json(response_data, filename)