import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import os
from PIL import Image
import base64
import streamlit.components.v1 as components

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

# Create a registration form
with st.form(key="registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    
    # Image upload
    uploaded_image = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])

    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        if name and email and phone and uploaded_image:
            # Save the uploaded image to a temporary location
            image = Image.open(uploaded_image)
            image_path = f"uploaded_images/{uploaded_image.name}"
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            image.save(image_path)
            
            # Convert the image to base64 (optional if you store URL elsewhere)
            with open(image_path, "rb") as img_file:
                encoded_image = base64.b64encode(img_file.read()).decode("utf-8")
            
            # You can upload the image to a cloud service and get the image URL here
            image_url = f"data:image/png;base64,{encoded_image}"  # You can replace this with the cloud URL
            
            # Add the data to the Google Sheet
            add_registration_to_sheet(name, email, phone, image_url)
            
            # Balloon effect using custom HTML
            components.html("""
                <style>
                    @keyframes balloonAnimation {
                        0% { transform: translateY(0); opacity: 1; }
                        100% { transform: translateY(-500px); opacity: 0; }
                    }
                    .balloon {
                        position: fixed;
                        bottom: 10px;
                        left: 50%;
                        width: 50px;
                        height: 50px;
                        background-color: #FF5733;
                        border-radius: 50%;
                        animation: balloonAnimation 3s ease-out forwards;
                    }
                </style>
                <div class="balloon"></div>
            """, height=100)
            
            # Reset form data using session state
            st.session_state.clear()  # Clears session state and resets the form

        else:
            st.error("Please fill in all the fields and upload an image.")
