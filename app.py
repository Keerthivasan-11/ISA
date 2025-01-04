import gspread
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import streamlit as st
import os

# The scopes required by the API to access Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly', 'https://www.googleapis.com/auth/drive']

# Path to your credentials.json file
CREDS_FILE = 'credentials.json'

# Function to authenticate and authorize using OAuth2
def authenticate_oauth2():
    creds = None
    # If we have saved credentials, load them
    if os.path.exists(CREDS_FILE):
        creds = Credentials.from_authorized_user_file(CREDS_FILE, SCOPES)
    
    # If no credentials or they are invalid, prompt the user to log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open(CREDS_FILE, 'w') as token:
            token.write(creds.to_json())
    
    # Use the credentials to authorize the client
    client = gspread.authorize(creds)
    return client

# Function to get data from a Google Sheet
def get_spreadsheet_data(spreadsheet_id, range_name):
    client = authenticate_oauth2()
    sheet = client.open_by_key(spreadsheet_id)
    worksheet = sheet.worksheet(range_name)
    data = worksheet.get_all_records()
    return data

# Example of calling the function
spreadsheet_id = "your_spreadsheet_id"
range_name = "Sheet1"
data = get_spreadsheet_data(spreadsheet_id, range_name)

# Displaying data in Streamlit
if data:
    st.write(data)
else:
    st.write("No data found.")
