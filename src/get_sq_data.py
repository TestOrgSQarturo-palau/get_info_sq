import requests
import json
import sys

# Get the command-line argument
arg1 = sys.argv[1] if len(sys.argv) > 1 else None
arg2 = sys.argv[2] if len(sys.argv) > 2 else None

def query_api(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        # Process the data here
        #print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

api_calls = {
    "license_usage": "/api/projects/license_usage",
    "quality_gates": "/api/qualitygates/list",
    "projects_latest_analysis": "/api/components/search_projects?f=analysisDate&s=analysisDate&asc=false",
    "projects_oldest_analysis": "/api/components/search_projects?f=analysisDate&s=analysisDate&asc=true",
    "permission_templates": "/api/permissions/search_templates",
    "quality_profiles": "/api/qualityprofiles/search"
}

# Use the argument in your code
if arg1 and arg2:
    if arg1.endswith('/'):
        arg1 = arg1[:-1]
    for key, value in api_calls.items():
        new_api_url = arg1 + value
        response_data = query_api(new_api_url, headers={"Authorization": "Bearer " + arg2})
        filename = key + ".json"
        save_to_json(response_data, filename)