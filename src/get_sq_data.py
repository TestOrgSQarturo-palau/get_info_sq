import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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



def add_to_google_sheet(data, sheet_name):
    # Define the scope and credentials for accessing the Google Sheet
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)

    # Authorize the credentials and open the Google Sheet
    client = gspread.authorize(credentials)
    sheet = client.open(sheet_name).sheet1

    # Append the data to the Google Sheet
    sheet.append_rows(data)

# Example usage
data = [
    ['Name', 'Age', 'Email'],
    ['John Doe', 30, 'john.doe@example.com'],
    ['Jane Smith', 25, 'jane.smith@example.com']
]
sheet_name = 'MySheet'
add_to_google_sheet(data, sheet_name)