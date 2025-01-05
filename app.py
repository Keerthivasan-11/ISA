import streamlit as st
import gspread
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

# Authenticate using credentials stored in secrets.toml
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = Credentials.from_service_account_info(st.secrets["gsheets"], scopes=scope)

# Use gspread to access Google Sheets
client = gspread.authorize(credentials)

# Access the spreadsheet using the URL from secrets.toml
spreadsheet_url = st.secrets["gsheets"]["spreadsheet_url"]
spreadsheet = client.open_by_url(spreadsheet_url)
worksheet = spreadsheet.worksheet("Sheet1")  # Replace "Registrations" with your worksheet name

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
