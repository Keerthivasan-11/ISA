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

# Function to validate email using regex
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Function to validate phone number using regex (simple validation for 10-digit phone numbers)
def is_valid_phone(phone):
    phone_regex = r'^\d{10}$'  # Assuming 10-digit phone numbers
    return re.match(phone_regex, phone)

# Authenticate and connect to Google Sheets using secrets
def connect_to_gsheet(spreadsheet_name, sheet_name):
    creds_json = st.secrets["gcp_service_account"]  # Access the credentials from secrets
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, SCOPE)
    client = gspread.authorize(credentials)
    spreadsheet = client.open(spreadsheet_name)  
    return spreadsheet.worksheet(sheet_name)  # Access specific sheet by name

# Function to add a new registration to the Google Sheet
def add_registration_to_sheet(name, email, phone, image_url, team_members, accommodation):
    try:
        # Clean up the team_members dictionary: only add non-empty members
        cleaned_team_members = {}
        for key, member in team_members.items():
            # Only include team members where 'name' is not empty
            if member["name"]:
                cleaned_team_members[key] = member
        
        # Connect to the Google Sheet
        sheet = connect_to_gsheet('Streamlit', 'Sheet1')
        
        # Append data to the Google Sheet (make sure team_members is valid)
        sheet.append_row([name, email, phone, image_url, str(cleaned_team_members), accommodation])
        st.success("Registration successful! Thank you for registering!")
    except Exception as e:
        st.error(f"Error while adding registration to sheet: {str(e)}")

# Streamlit app to create the registration form
st.title("Event Registration Form")

# Important note at the top
st.markdown("""
    **IMPORTANT NOTE**: 
    Please note that **NO prelims will be conducted** for the *Indian Engineers Elite Challenge 2025*.

    **Registration Fees**:
    - **1,500 INR** with ISA Student membership (All team members must be ISA members).
    - **2,000 INR** without ISA Student membership.
    
    **Payment Instructions**:
    - While paying, add your *team name* and *college name* in the payment notes.
    - After successful transaction, attach the screenshot in the last section of the form before submitting.

    **Please ensure you fill both the Google Form and the website form to complete your registration**. 
    (⭐️ = Mandatory fields)
""")

# Initialize session state for form fields
if 'name' not in st.session_state:
    st.session_state.name = ''
    st.session_state.email = ''
    st.session_state.phone = ''
    st.session_state.uploaded_image = None
    st.session_state.submitted = False
    st.session_state.team_member_1_name = ''
    st.session_state.team_member_1_year = ''
    st.session_state.team_member_1_department = ''
    st.session_state.team_member_2_name = ''
    st.session_state.team_member_2_year = ''
    st.session_state.team_member_2_department = ''
    st.session_state.team_member_3_name = ''
    st.session_state.team_member_3_year = ''
    st.session_state.team_member_3_department = ''
    st.session_state.accommodation = ''
    st.session_state.team_members = []

# Show the image from the URL before submitting
image_url = "https://github.com/Keerthivasan-11/ISA/blob/main/WhatsApp%20Image%202025-01-10%20at%2022.29.36.jpeg?raw=true"
st.image(image_url, caption="Please view the image before submitting your registration", use_column_width=True)

# Create a registration form
with st.form(key="registration_form"):
    st.session_state.name = st.text_input("Full Name", st.session_state.name)
    st.session_state.email = st.text_input("Email Address", st.session_state.email, help="Enter a valid email address (e.g., example@domain.com)")
    st.session_state.phone = st.text_input("Phone Number", st.session_state.phone, help="Enter a 10-digit phone number.")
    
    # Team Members Information
    st.session_state.team_member_1_name = st.text_input("Team Member 1 Name", st.session_state.team_member_1_name)
    st.session_state.team_member_1_year = st.text_input("Team Member 1 Year of Study", st.session_state.team_member_1_year)
    st.session_state.team_member_1_department = st.text_input("Team Member 1 Department", st.session_state.team_member_1_department)
    
    st.session_state.team_member_2_name = st.text_input("Team Member 2 Name", st.session_state.team_member_2_name)
    st.session_state.team_member_2_year = st.text_input("Team Member 2 Year of Study", st.session_state.team_member_2_year)
    st.session_state.team_member_2_department = st.text_input("Team Member 2 Department", st.session_state.team_member_2_department)
    
    # Optional Team Member 3
    st.session_state.team_member_3_name = st.text_input("Team Member 3 Name (Optional)", st.session_state.team_member_3_name)
    st.session_state.team_member_3_year = st.text_input("Team Member 3 Year of Study (Optional)", st.session_state.team_member_3_year)
    st.session_state.team_member_3_department = st.text_input("Team Member 3 Department (Optional)", st.session_state.team_member_3_department)
    
    # ISA Membership ID
    isa_member_1 = st.text_input("ISA ID for Team Member 1 (if applicable)", "")
    isa_member_2 = st.text_input("ISA ID for Team Member 2 (if applicable)", "")
    isa_member_3 = st.text_input("ISA ID for Team Member 3 (if applicable)", "")
    
    # Image upload with preview
    st.session_state.uploaded_image = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])
    
    if st.session_state.uploaded_image:
        image = Image.open(st.session_state.uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Accommodation choice
    st.session_state.accommodation = st.selectbox("Do you need Hostel Accommodation?", ["Yes", "No"])

    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        # Validate the email and phone number
        if not is_valid_email(st.session_state.email):
            st.error("Please enter a valid email address.")
        elif not is_valid_phone(st.session_state.phone):
            st.error("Please enter a valid 10-digit phone number.")
        elif st.session_state.name and st.session_state.email and st.session_state.phone and st.session_state.uploaded_image and \
           st.session_state.team_member_1_name and st.session_state.team_member_1_year and st.session_state.team_member_1_department and \
           st.session_state.team_member_2_name and st.session_state.team_member_2_year and st.session_state.team_member_2_department:
            
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
            
            # Collect team member details
            team_members = {
                "Team Member 1": {
                    "name": st.session_state.team_member_1_name,
                    "year": st.session_state.team_member_1_year,
                    "department": st.session_state.team_member_1_department,
                    "isa_id": isa_member_1
                },
                "Team Member 2": {
                    "name": st.session_state.team_member_2_name,
                    "year": st.session_state.team_member_2_year,
                    "department": st.session_state.team_member_2_department,
                    "isa_id": isa_member_2
                }
            }
            
            if st.session_state.team_member_3_name:  # If Team Member 3 is filled
                team_members["Team Member 3"] = {
                    "name": st.session_state.team_member_3_name,
                    "year": st.session_state.team_member_3_year,
                    "department": st.session_state.team_member_3_department,
                    "isa_id": isa_member_3
                }
            
            # Add the data to the Google Sheet
            add_registration_to_sheet(st.session_state.name, st.session_state.email, st.session_state.phone, image_url, team_members, st.session_state.accommodation)
            
            # Show the balloon effect after successful registration
            st.balloons()  # Trigger the balloon effect

            # Generate the QR code for the confirmation or registration
            qr_data = f"Registration Successful for {st.session_state.name}"
            qr_img = qrcode.make(qr_data)
            qr_img_path = "qr_code.png"
            qr_img.save(qr_img_path)
            
            # Show the QR code at the end
            st.image(qr_img_path, caption="Scan the QR Code for Registration Confirmation", use_column_width=True)

            # Set the session state to indicate that the form was submitted
            st.session_state.submitted = True

        else:
            st.error("Please fill in all the compulsory fields and upload an image.")
