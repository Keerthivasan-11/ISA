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
    # Retrieve credentials from Streamlit secrets
    creds_json = st.secrets["gcp_service_account"]  # Access the credentials from secrets

    # Use the credentials from the secrets file (as dictionary)
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, SCOPE)
    
    # Authorize the credentials
    client = gspread.authorize(credentials)
    spreadsheet = client.open(spreadsheet_name)  
    return spreadsheet.worksheet(sheet_name)  # Access specific sheet by name

# Function to add a new registration to the Google Sheet
def add_registration_to_sheet(name, email, phone, image_url):
    # Connect to the Google Sheet
    sheet = connect_to_gsheet('Streamlit', 'Sheet1')

    # Add the new registration data to the sheet (assuming columns: Name, Email, Phone, Image)
    sheet.append_row([name, email, phone, image_url])

# Streamlit app to create the registration form
st.title("Event Registration Form")

# Create a registration form
with st.form(key="registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    
    # Image upload
    uploaded_image = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])

    # Add a submit button to the form
    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        if name and email and phone and uploaded_image:
            # Save the uploaded image to a temporary location
            image = Image.open(uploaded_image)
            image_path = f"uploaded_images/{uploaded_image.name}"
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            image.save(image_path)
            
            # Convert the image to base64 (if you want to store it as an image URL)
            with open(image_path, "rb") as img_file:
                encoded_image = base64.b64encode(img_file.read()).decode("utf-8")
            
            # Here we store the base64 encoded image or the image path depending on your needs.
            # In this example, I'm storing the base64-encoded image as the image URL.
            image_url = f"data:image/png;base64,{encoded_image}"
            
            # Add the data to the Google Sheet
            add_registration_to_sheet(name, email, phone, image_url)
            
            # Display a success message and simulate the balloon effect
            st.success("Registration successful! 🎈🎉")
            
            # Wait for 3 seconds to simulate the effect before resetting the form
            time.sleep(3)
            
            # Reset the form (clear inputs for next user)
            st.experimental_rerun()
        else:
            st.error("Please fill in all the fields and upload an image.")
