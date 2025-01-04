import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authentication and Google Sheets connection
def authenticate_gspread():
    # Define the scope of the application
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Use your downloaded JSON credentials file
    creds = ServiceAccountCredentials.from_json_keyfile_name('your_credentials.json', scope)
    client = gspread.authorize(creds)
    
    # Open the Google Sheet (replace with your sheet name)
    sheet = client.open("ISA Hackathon Registrations").sheet1
    return sheet

# Streamlit UI
def app():
    st.title('ISA Hackathon Registration')
    
    # Display event details
    st.write("""
    Welcome to the ISA Hackathon! Please fill in the form below to register.
    """)

    # Registration form
    with st.form(key='registration_form'):
        name = st.text_input('Full Name')
        email = st.text_input('Email Address')
        team_name = st.text_input('Team Name')
        phone = st.text_input('Phone Number')
        
        submit_button = st.form_submit_button(label='Register')

        if submit_button:
            # Authenticate and get Google Sheets client
            sheet = authenticate_gspread()

            # Append data to the sheet
            sheet.append_row([name, email, team_name, phone])

            st.write(f"Registration successful for {name}!")

if __name__ == '__main__':
    app()
