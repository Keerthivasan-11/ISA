import toml
import gspread
from google.oauth2.service_account import Credentials
import streamlit as st

# Load credentials from secrets.toml
def load_secrets():
    secrets = toml.load(".streamlit/secrets.toml")["connections"]["gsheets"]
    return secrets

# Load the secrets from the TOML file
secrets = load_secrets()

# Prepare credentials dictionary
credentials_dict = {
    "type": secrets["type"],
    "project_id": secrets["project_id"],
    "private_key_id": secrets["private_key_id"],
    "private_key": secrets["private_key"],
    "client_email": secrets["client_email"],
    "client_id": secrets["client_id"],
    "auth_uri": secrets["auth_uri"],
    "token_uri": secrets["token_uri"],
    "auth_provider_x509_cert_url": secrets["auth_provider_x509_cert_url"],
    "client_x509_cert_url": secrets["client_x509_cert_url"]
}

# Authenticate using service account credentials
credentials = Credentials.from_service_account_info(credentials_dict, scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])

# Use gspread to access Google Sheets
client = gspread.authorize(credentials)

# Access the spreadsheet
spreadsheet_url = secrets["spreadsheet"]
spreadsheet = client.open_by_url(spreadsheet_url)
worksheet = spreadsheet.worksheet("Registrations")

# Registration Form
st.title("ISA Hackathon Registration")
with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    team_name = st.text_input("Team Name")
    submitted = st.form_submit_button("Register")

    if submitted:
        if name and email and team_name:
            worksheet.append_row([name, email, team_name])
            st.success("You have successfully registered!")
        else:
            st.error("Please fill in all the fields.")
