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

# Function to add a new registration to the Google Sheet
def add_registration_to_sheet(name, email, phone):
    # Connect to the Google Sheet
    sheet = connect_to_gsheet('Streamlit', 'Sheet1')

    # Add the new registration data to the sheet (assuming columns: Name, Email, Phone)
    sheet.append_row([name, email, phone])

# Streamlit app to create the registration form
st.title("Event Registration Form")

# Create a registration form
with st.form(key="registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    
    # Add a submit button to the form
    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        if name and email and phone:
            # Add the data to the Google Sheet
            add_registration_to_sheet(name, email, phone)
            st.success("Registration successful!")
        else:
            st.error("Please fill in all the fields.")
