import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import os
from PIL import Image
import base64
import streamlit.components.v1 as components
import random
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

# Function to show the balloon effect
def show_balloon_effect():
    balloon_count = random.randint(5, 10)  # Random number of balloons
    balloon_html = """
        <style>
            @keyframes balloonAnimation {
                0% { transform: translateY(0); opacity: 1; }
                100% { transform: translateY(-500px); opacity: 0; }
            }
            .balloon {
                position: fixed;
                bottom: 10px;
                width: 50px;
                height: 50px;
                border-radius: 50%;
                animation: balloonAnimation 3s ease-out forwards;
            }
            /* Add random colors to the balloons */
            .balloon:nth-child(1) { background-color: #FF5733; }
            .balloon:nth-child(2) { background-color: #33FF57; }
            .balloon:nth-child(3) { background-color: #3357FF; }
            .balloon:nth-child(4) { background-color: #F0E68C; }
            .balloon:nth-child(5) { background-color: #FF6347; }
            .balloon:nth-child(6) { background-color: #D2691E; }
            .balloon:nth-child(7) { background-color: #ADFF2F; }
            .balloon:nth-child(8) { background-color: #8A2BE2; }
            .balloon:nth-child(9) { background-color: #00CED1; }
            .balloon:nth-child(10) { background-color: #FF1493; }
        </style>
    """
    # Add multiple balloons to the page
    for _ in range(balloon_count):
        components.html(balloon_html, height=100)

# Streamlit app to create the registration form
st.title("Event Registration Form")

# Use session state to track if the form is submitted
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

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
            
            # Show the balloon effect after successful registration
            show_balloon_effect()

            # Mark the form as submitted
            st.session_state.submitted = True

        else:
            st.error("Please fill in all the fields and upload an image.")

# If form is submitted, reset the state after a delay to allow the user to submit again
if st.session_state.submitted:
    time.sleep(3)  # Delay to let balloons show
    st.session_state.submitted = False  # Reset the submission flag
    st.experimental_rerun()  # Rerun the app to allow the next user to fill the form
