import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# Define the scope for Google Sheets and Drive
SCOPE = [
    "https://spreadsheets.google.com/feeds", 
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file", 
    "https://www.googleapis.com/auth/drive"
]

# Authenticate and connect to Google Sheets using secrets
def connect_to_gsheet(spreadsheet_name, sheet_name):
    # Retrieve credentials from Streamlit secrets
    creds_json = st.secrets["gcp_service_account"]  # Access the credentials from secrets

    # Use the credentials from the secrets file (as dictionary)
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, SCOPE)
    
    # Authorize the credentials
    client = gspread.authorize(credentials)
    spreadsheet = client.open(spreadsheet_name)  
    return spreadsheet.worksheet(sheet_name)  # Access specific sheet by name

# Example usage
spreadsheet_name = 'Streamlit'
sheet_name = 'Sheet1'

# Connect to the Google Sheet
sheet_by_name = connect_to_gsheet(spreadsheet_name, sheet_name)

# Continue with your Streamlit app
st.title("Tasks Form")
