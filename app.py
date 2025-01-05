import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import streamlit as st

# Title and description
st.title("ISA Hackathon Registration")
st.markdown("Welcome to the registration portal for the ISA Hackathon. Fill in the details below to register your team!")

# Set up Google Sheets API credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gsheets"], scope)
client = gspread.authorize(creds)

# Open the Google Sheet and fetch data
sheet = client.open("ISA Hackathon Registration").worksheet("Registrations")
existing_data = pd.DataFrame(sheet.get_all_records())

# Function for email validation
def is_valid_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

# Function for phone number validation (assuming 10 digits)
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

# Registration Form
st.markdown("### Participant Registration Form")
with st.form(key="registration_form"):
    team_name = st.text_input(label="Team Name*")
    participant_name = st.text_input(label="Participant Name*")
    email = st.text_input(label="Email Address*")
    phone = st.text_input(label="Phone Number*")
    institution = st.text_input(label="Institution Name*")
    additional_info = st.text_area(label="Additional Notes (optional)")

    submit_button = st.form_submit_button(label="Register")

    if submit_button:
        # Validation
        if not team_name or not participant_name or not email or not phone or not institution:
            st.warning("Please fill in all mandatory fields marked with *.")
        elif not is_valid_email(email):
            st.warning("Please enter a valid email address.")
        elif not is_valid_phone(phone):
            st.warning("Please enter a valid 10-digit phone number.")
        elif existing_data["Email"].str.contains(email, case=False, na=False).any():
            st.warning("This email is already registered!")
        else:
            # Save registration details
            registration_data = pd.DataFrame(
                [
                    {
                        "TeamName": team_name,
                        "ParticipantName": participant_name,
                        "Email": email,
                        "Phone": phone,
                        "Institution": institution,
                        "AdditionalInfo": additional_info,
                    }
                ]
            )
            # Append new data to the sheet
            sheet.append_rows(registration_data.values.tolist())
            st.success("Registration successful! Thank you for registering for the ISA Hackathon.")

# View All Registrations (Admin View)
if st.checkbox("View All Registrations (Admin Only)"):
    st.dataframe(existing_data)
