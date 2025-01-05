import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Authenticate and connect to Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gsheets"], scope)
client = gspread.authorize(credentials)

# Open the Google Spreadsheet
spreadsheet = client.open_by_url(st.secrets["gsheets"]["spreadsheet_url"])
worksheet = spreadsheet.worksheet("Registrations")  # Make sure the worksheet exists

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
