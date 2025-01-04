import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Directly embed the JSON credentials in the code
credentials_json = {
    "web": {
        "client_id": "39633506830-9n7121fp8qh6a9tvv0h4mnhr871bv4ht.apps.googleusercontent.com",
        "project_id": "static-destiny-446816-f4",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "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"
    }
}

# Convert the dictionary to JSON and store it as a string
credentials_json_str = json.dumps(credentials_json)

# Authenticate using the credentials from the JSON string
def authenticate_google_sheets():
    credentials_info = json.loads(credentials_json_str)
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        credentials_info, scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    )

    client = gspread.authorize(credentials)
    return client

# Function to save person details to Google Sheets
def save_to_google_sheet(data):
    client = authenticate_google_sheets()
    sheet = client.open('Your Google Sheet Name').sheet1  # Replace with your actual Google Sheet name
    sheet.append_row(data)  # Appends the details as a new row

# Streamlit User Interface for collecting personal details
def main():
    st.title("Person Details Form")

    # Form to collect user details
    with st.form(key='person_form'):
        name = st.text_input("Enter Name")
        age = st.number_input("Enter Age", min_value=1)
        email = st.text_input("Enter Email")
        phone = st.text_input("Enter Phone Number")

        # Submit button
        submit_button = st.form_submit_button("Save Details")

        if submit_button:
            if name and age and email and phone:
                # Prepare data to be saved
                data = [name, age, email, phone]
                save_to_google_sheet(data)
                st.success(f"Details for {name} saved successfully!")
            else:
                st.error("Please fill all the details.")

# Run the app
if __name__ == "__main__":
    main()
