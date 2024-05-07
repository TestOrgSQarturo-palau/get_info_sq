import gspread
from oauth2client.service_account import ServiceAccountCredentials



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