import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import os
from PIL import Image
import base64
import re

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
def add_registration_to_sheet(name, email, phone, image_url, team_members, accommodation, payment_screenshot):
    try:
        sheet = connect_to_gsheet('Streamlit', 'Sheet1')
        sheet.append_row([name, email, phone, image_url, team_members, accommodation, payment_screenshot])
        st.success("Registration successful!")
    except Exception as e:
        st.error(f"Error while adding registration to sheet: {str(e)}")

# Validate phone number with more flexibility
def is_valid_phone(phone):
    phone_regex = r'^\+?[1-9]\d{1,14}$'  # International format: +[country code] + number
    return re.match(phone_regex, phone)

# Validate email with more accuracy
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zAZ0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Streamlit app for registration form
st.title("Event Registration Form")

# Input validation hints
st.write("### Help")
st.write("- Email: Enter a valid email address (example@domain.com)")
st.write("- Phone: Enter your phone number (use international format if needed)")

# Conditional team member fields (optional member only shows if required)
show_team_member_3 = st.checkbox("Add Team Member 3")

# Main form
with st.form(key="registration_form"):
    # Personal details
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    
    # Team members (compulsory fields)
    team_member_1_name = st.text_input("Team Member 1 Name")
    team_member_2_name = st.text_input("Team Member 2 Name")
    
    if show_team_member_3:
        team_member_3_name = st.text_input("Team Member 3 Name (Optional)")
    
    # Display image preview after upload
    uploaded_image = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Accommodation choice
    accommodation = st.selectbox("Do you need Hostel Accommodation?", ["Yes", "No"])

    # Payment Screenshot upload
    payment_screenshot = st.file_uploader("Upload Payment Screenshot", type=["jpg", "png", "jpeg"])

    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        # Validate email and phone fields with real-time feedback
        if not is_valid_email(email):
            st.error("Invalid email address. Please enter a valid email.")
        elif not is_valid_phone(phone):
            st.error("Invalid phone number. Please enter a valid phone number.")
        elif not uploaded_image:
            st.error("Please upload your image.")
        elif not payment_screenshot:
            st.error("Please upload the payment screenshot.")
        else:
            # Save the uploaded image to a temporary location
            image_path = f"uploaded_images/{uploaded_image.name}"
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            with open(image_path, "wb") as f:
                f.write(uploaded_image.getbuffer())

            # Convert the image to base64 (optional if you store URL elsewhere)
            with open(image_path, "rb") as img_file:
                encoded_image = base64.b64encode(img_file.read()).decode("utf-8")
            
            # You can upload the image to a cloud service and get the image URL here
            image_url = f"data:image/png;base64,{encoded_image}"

            # Gather team member names
            team_members = f"{team_member_1_name}, {team_member_2_name}"
            if show_team_member_3:
                team_members += f", {team_member_3_name}"

            # Add the data to the Google Sheet
            add_registration_to_sheet(name, email, phone, image_url, team_members, accommodation, payment_screenshot)

            # Show the balloon effect after successful registration
            st.balloons()  # Trigger the balloon effect

            # Confirmation message
            st.success("Form submitted successfully! Thank you for registering.")
            
            # Reset form fields (if necessary)
            st.session_state.submitted = True

# Add QR code image at the end of the form
st.write("### Payment QR Code")
# Use the raw link to your QR code image hosted on GitHub
qr_code_image_url = "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/WhatsApp%20Image%202025-01-10%20at%2022.29.36.jpeg"
st.image(qr_code_image_url, caption="Scan to Pay", use_column_width=True)
