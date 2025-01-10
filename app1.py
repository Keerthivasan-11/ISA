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
    balloon_count = random.randint(30, 50)  # Increase the range to get 30-50 balloons
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
                animation: balloonAnimation 4s ease-out forwards;
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
            .balloon:nth-child(11) { background-color: #7FFF00; }
            .balloon:nth-child(12) { background-color: #FF4500; }
            .balloon:nth-child(13) { background-color: #DAA520; }
            .balloon:nth-child(14) { background-color: #9932CC; }
            .balloon:nth-child(15) { background-color: #FFD700; }
            .balloon:nth-child(16) { background-color: #8B0000; }
            .balloon:nth-child(17) { background-color: #228B22; }
            .balloon:nth-child(18) { background-color: #8B4513; }
            .balloon:nth-child(19) { background-color: #483D8B; }
            .balloon:nth-child(20) { background-color: #D3D3D3; }
            .balloon:nth-child(21) { background-color: #C71585; }
            .balloon:nth-child(22) { background-color: #2E8B57; }
            .balloon:nth-child(23) { background-color: #B22222; }
            .balloon:nth-child(24) { background-color: #20B2AA; }
            .balloon:nth-child(25) { background-color: #4B0082; }
            .balloon:nth-child(26) { background-color: #FFC0CB; }
            .balloon:nth-child(27) { background-color: #00FA9A; }
            .balloon:nth-child(28) { background-color: #A52A2A; }
            .balloon:nth-child(29) { background-color: #0000CD; }
            .balloon:nth-child(30) { background-color: #F08080; }
            .balloon:nth-child(31) { background-color: #FF00FF; }
            .balloon:nth-child(32) { background-color: #32CD32; }
            .balloon:nth-child(33) { background-color: #4169E1; }
            .balloon:nth-child(34) { background-color: #FFFF00; }
            .balloon:nth-child(35) { background-color: #FF8C00; }
            .balloon:nth-child(36) { background-color: #800080; }
            .balloon:nth-child(37) { background-color: #808000; }
            .balloon:nth-child(38) { background-color: #A9A9A9; }
            .balloon:nth-child(39) { background-color: #2F4F4F; }
            .balloon:nth-child(40) { background-color: #7CFC00; }
            .balloon:nth-child(41) { background-color: #BC8F8F; }
            .balloon:nth-child(42) { background-color: #FFB6C1; }
            .balloon:nth-child(43) { background-color: #D8BFD8; }
            .balloon:nth-child(44) { background-color: #FF4500; }
            .balloon:nth-child(45) { background-color: #32CD32; }
            .balloon:nth-child(46) { background-color: #ADD8E6; }
            .balloon:nth-child(47) { background-color: #98FB98; }
            .balloon:nth-child(48) { background-color: #FF1493; }
            .balloon:nth-child(49) { background-color: #FF6347; }
            .balloon:nth-child(50) { background-color: #FFFACD; }
        </style>
    """
    # Add multiple balloons to the page
    for _ in range(balloon_count):
        components.html(balloon_html, height=100)

# Streamlit app to create the registration form
st.title("Event Registration Form")

# Create a session state to track form submission
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
            st.session_state.submitted = True

        else:
            st.error("Please fill in all the fields and upload an image.")

# Display the balloon effect if the form has been submitted
if st.session_state.submitted:
    show_balloon_effect()
    st.session_state.submitted = False  # Reset the flag for next submission
