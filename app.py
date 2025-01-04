import gspread
from oauth2client.client import OAuth2WebServerFlow
import streamlit as st
from oauth2client.file import Storage
from oauth2client.tools import run_flow

# Replace the following credentials with your client ID and client secret from Google Cloud Console
CLIENT_ID = '39633506830-9n7121fp8qh6a9tvv0h4mnhr871bv4ht.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REDIRECT_URI = 'http://localhost:8501'  # Use your Streamlit app's URL

# Scope to access Google Sheets
SCOPE = ['https://www.googleapis.com/auth/spreadsheets.readonly', 'https://www.googleapis.com/auth/drive']

# Create an OAuth2 flow object
flow = OAuth2WebServerFlow(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scope=SCOPE, redirect_uri=REDIRECT_URI)

# Function to authenticate using OAuth2
def authenticate_oauth2():
    storage = Storage('credentials.json')
    credentials = storage.get()

    if not credentials or credentials.invalid:
        credentials = run_flow(flow, storage)
    
    client = gspread.authorize(credentials)
    return client

# Example function to access Google Sheets data
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
