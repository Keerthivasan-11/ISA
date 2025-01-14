import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import os
from PIL import Image
import re

def app():
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

    # Function to display the GPay QR code at the bottom of each page
    def display_gpay_qr():
        st.markdown("### 🏦 **GPay QR Code for Payment**")
        gpay_qr_url = "https://github.com/Keerthivasan-11/ISA/blob/main/Gpay%20qr.jpeg?raw=true"
        st.image(gpay_qr_url, caption="Scan to Pay using GPay", use_column_width=True)

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
            cleaned_team_members = {
                key: member for key, member in team_members.items() if member["name"]
            }
            
            # Connect to the Google Sheet
            sheet = connect_to_gsheet('Streamlit', 'Sheet1')
            
            # Append data to the Google Sheet
            sheet.append_row([name, email, phone, image_url, str(cleaned_team_members), accommodation])
            st.success("🎉 Registration successful! Thank you for registering! 🎉")
        except Exception as e:
            st.error(f"⚠️ Error while adding registration to sheet: {str(e)}")

    # Streamlit app to create the registration form
    st.title("🌟 Event Registration Form 🌟")
    st.markdown("""
        ### 📌 **IMPORTANT NOTE** 
        - Please note that **NO prelims will be conducted** for the *Indian Engineers Elite Challenge 2025*.
        - Make sure to fill both **Google Form** and this **Website Form** to complete your registration.
        
        ### 💸 **Registration Fees**:
        - **1,500 INR** with ISA Student membership (All team members must be ISA members).
        - **2,000 INR** without ISA Student membership.
        
        ### 📝 **Instructions for Payment**:
        - Include your *team name* and *college name* in the payment notes while paying.
        - After payment, scan the **GPay QR code** (displayed at the end) for reference.

        ⭐️ **Fields marked with a star are mandatory.**
    """)

    # Initialize session state for form fields
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    # Create a registration form
    with st.form(key="registration_form"):
        st.text_input("⭐️ Full Name", key="name")
        st.text_input("⭐️ Email Address", key="email", help="Enter a valid email address (e.g., example@domain.com)")
        st.text_input("⭐️ Phone Number", key="phone", help="Enter a 10-digit phone number.")

        st.markdown("#### 👥 **Team Members**")
        st.text_input("⭐️ Team Member 1 Name", key="team_member_1_name")
        st.text_input("⭐️ Team Member 1 Year of Study", key="team_member_1_year")
        st.text_input("⭐️ Team Member 1 Department", key="team_member_1_department")

        st.text_input("⭐️ Team Member 2 Name", key="team_member_2_name")
        st.text_input("⭐️ Team Member 2 Year of Study", key="team_member_2_year")
        st.text_input("⭐️ Team Member 2 Department", key="team_member_2_department")

        st.text_input("Team Member 3 Name (Optional)", key="team_member_3_name")
        st.text_input("Team Member 3 Year of Study (Optional)", key="team_member_3_year")
        st.text_input("Team Member 3 Department (Optional)", key="team_member_3_department")
        st.markdown("### 🏦 **GPay QR Code for Payment**")
        gpay_qr_url = "https://github.com/Keerthivasan-11/ISA/blob/main/Gpay%20qr.jpeg?raw=true"
        st.image(gpay_qr_url, caption="Scan to Pay using GPay", use_column_width=True)
        st.markdown("#### 🏠 **⭐️Accommodation**")
        st.selectbox("Do you need Hostel Accommodation?", ["Yes", "No"], key="accommodation")
       
        st.markdown("#### 🖼️ **Payment Proof Upload **")
        uploaded_image = st.file_uploader("Upload your payment screenshot (JPG/PNG only, optional)", type=["jpg", "png", "jpeg"])
        
        submit_button = st.form_submit_button(label="🚀 Submit")
        
        if submit_button:
            # Validate the email and phone number
            if not is_valid_email(st.session_state.email):
                st.error("⚠️ Please enter a valid email address.")
            elif not is_valid_phone(st.session_state.phone):
                st.error("⚠️ Please enter a valid 10-digit phone number.")
            else:
                # Process registration
                team_members = {
                    "Team Member 1": {
                        "name": st.session_state.team_member_1_name,
                        "year": st.session_state.team_member_1_year,
                        "department": st.session_state.team_member_1_department,
                    },
                    "Team Member 2": {
                        "name": st.session_state.team_member_2_name,
                        "year": st.session_state.team_member_2_year,
                        "department": st.session_state.team_member_2_department,
                    },
                    "Team Member 3": {
                        "name": st.session_state.team_member_3_name,
                        "year": st.session_state.team_member_3_year,
                        "department": st.session_state.team_member_3_department,
                    },
                }

                # Optional: Handle the uploaded image
                image_url = "No Image Uploaded"
                if uploaded_image:
                    image = Image.open(uploaded_image)
                    image_url = f"uploaded_images/{uploaded_image.name}"
                    os.makedirs("uploaded_images", exist_ok=True)
                    image.save(image_url)

                # Add to Google Sheet
                add_registration_to_sheet(
                    st.session_state.name,
                    st.session_state.email,
                    st.session_state.phone,
                    image_url,
                    team_members,
                    st.session_state.accommodation,
                )
                # Display success
                st.balloons()
                st.success("🎉 Your registration has been successfully submitted!")
                
    
