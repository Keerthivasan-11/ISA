import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import os
from PIL import Image
import base64
import time

# Define the scope for Google Sheets and Drive
SCOPE = [
    "https://spreadsheets.google.com/feeds", 
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file", 
    "https://www.googleapis.com/auth/drive"
]

# Authenticate and connect to Google Sheets using secrets
def connect_to_gsheet(spreadsheet_name, sheet_name):
    creds_json = st.secrets["gcp_service_account"]  # Access the credentials from secrets
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, SCOPE)
    client = gspread.authorize(credentials)
    spreadsheet = client.open(spreadsheet_name)  
    return spreadsheet.worksheet(sheet_name)  # Access specific sheet by name

# Function to add a new registration to the Google Sheet
def add_registration_to_sheet(name, email, phone, image_url):
    try:
        sheet = connect_to_gsheet('Streamlit', 'Sheet1')
        sheet.append_row([name, email, phone, image_url])
        st.success("Registration successful!")
    except Exception as e:
        st.error(f"Error while adding registration to sheet: {str(e)}")

# Streamlit app to create the registration form
st.title("Event Registration Form")

# Initialize session state for form fields
if 'name' not in st.session_state:
    st.session_state.name = ''
    st.session_state.email = ''
    st.session_state.phone = ''
    st.session_state.uploaded_image = None
    st.session_state.submitted = False

# Create a registration form
with st.form(key="registration_form"):
    st.session_state.name = st.text_input("Full Name", st.session_state.name)
    st.session_state.email = st.text_input("Email Address", st.session_state.email)
    st.session_state.phone = st.text_input("Phone Number", st.session_state.phone)
    
    # Image upload
    st.session_state.uploaded_image = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])

    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        if st.session_state.name and st.session_state.email and st.session_state.phone and st.session_state.uploaded_image:
            # Save the uploaded image to a temporary location
            image = Image.open(st.session_state.uploaded_image)
            image_path = f"uploaded_images/{st.session_state.uploaded_image.name}"
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            image.save(image_path)
            
            # Convert the image to base64 (optional if you store URL elsewhere)
            with open(image_path, "rb") as img_file:
                encoded_image = base64.b64encode(img_file.read()).decode("utf-8")
            
            # You can upload the image to a cloud service and get the image URL here
            image_url = f"data:image/png;base64,{encoded_image}"  # You can replace this with the cloud URL
            
            # Add the data to the Google Sheet
            add_registration_to_sheet(st.session_state.name, st.session_state.email, st.session_state.phone, image_url)
            
            # Show the balloon effect after successful registration
            st.balloons()  # Trigger the balloon effect

            # Set the session state to indicate that the form was submitted
            st.session_state.submitted = True

        else:
            st.error("Please fill in all the fields and upload an image.")

# Reset the form fields after submission, and simulate a page reload using session_state logic
if st.session_state.submitted:
    # Wait for a few seconds before resetting the form
    time.sleep(2)  # Optional: Add delay for better user experience
    st.session_state.submitted = False  # Reset the submission state
    st.session_state.name = ''
    st.session_state.email = ''
    st.session_state.phone = ''
    st.session_state.uploaded_image = None  # Clear the uploaded image

    # This effectively resets the form without re-running the entire app
     # Trigger a page "reload" after clearing the state
