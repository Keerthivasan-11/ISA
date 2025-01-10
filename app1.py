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

# Add registration data to the Google Sheet
def add_registration_to_sheet(name, email, phone, image_url):
    try:
        # Connect to the sheet
        sheet = connect_to_gsheet('Streamlit', 'Sheet1')
        # Append the row to the sheet
        sheet.append_row([name, email, phone, image_url])
        st.success("Registration added successfully!")
    except gspread.exceptions.APIError as e:
        st.error(f"Error adding registration: {e}")
        st.error(f"API error details: {e.args}")

# Streamlit form
st.title("Registration Form")

# User inputs
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# Process the form
if st.button("Submit"):
    if name and email and phone and image:
        # Process image (uploading it to a static URL or handling it in some way)
        # For now, we'll just display the image URL
        image_url = image.name  # This can be improved to upload to a server
        add_registration_to_sheet(name, email, phone, image_url)
    else:
        st.error("Please fill in all fields.")
