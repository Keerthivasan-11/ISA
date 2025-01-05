import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Title and description
st.title("ISA Hackathon Registration")
st.markdown("Welcome to the registration portal for the ISA Hackathon. Fill in the details below to register your team!")

# Google Sheets Authentication Setup
def authenticate_gsheet():
    # Define the scope of the API access
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Provide the path to your service account key file
    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        st.secrets["gsheets"], scope
    )
    
    # Authenticate and return the client
    client = gspread.authorize(creds)
    return client

# Establishing connection to the Google Sheet
client = authenticate_gsheet()
sheet = client.open_by_url(st.secrets["gsheets"]["spreadsheet"])
worksheet = sheet.worksheet("Registrations")

# Fetch existing registration data
existing_data = pd.DataFrame(worksheet.get_all_records())
existing_data = existing_data.dropna(how="all")  # Drop empty rows

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
            updated_df = pd.concat([existing_data, registration_data], ignore_index=True)

            # Update Google Sheet with new data
            for index, row in updated_df.iterrows():
                worksheet.append_row(row.values.tolist())

            st.success("Registration successful! Thank you for registering for the ISA Hackathon.")

# View All Registrations (Admin View)
if st.checkbox("View All Registrations (Admin Only)"):
    st.dataframe(existing_data)
