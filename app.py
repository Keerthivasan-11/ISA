import streamlit as st
import gspread
from google.auth import credentials
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

# Authentication and Google Sheets connection
def authenticate_gspread():
    # Load the credentials from the service account JSON file
    creds = None
    if st.secrets.get('gspread_service_account'):
        creds = Credentials.from_service_account_info(
            st.secrets["gspread_service_account"],
            scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
        )

    # If there are no (valid) credentials available, prompt the user to log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            st.error("Failed to authenticate. Please check your credentials.")
            return None

    return gspread.authorize(creds)

# Example function to access Google Sheets data
def get_spreadsheet_data(spreadsheet_id, range_name):
    client = authenticate_gspread()
    if client:
        sheet = client.open_by_key(spreadsheet_id)
        worksheet = sheet.worksheet(range_name)
        data = worksheet.get_all_records()
        return data
    else:
        return []

# Example of calling the function
spreadsheet_id = "your_spreadsheet_id"
range_name = "Sheet1"
data = get_spreadsheet_data(spreadsheet_id, range_name)

# Displaying data in Streamlit
if data:
    st.write(data)
else:
    st.write("No data found.")
