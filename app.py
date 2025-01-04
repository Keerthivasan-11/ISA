import os
import streamlit as st
from firebase_admin import credentials, initialize_app, db
from datetime import datetime

# Initialize Firebase app
if not os.path.exists("firebase_admin_initialized.txt"):  # Avoid reinitialization during hot reload
    service_account_path = os.getenv("FIREBASE_ADMIN_JSON")  # Path from environment variable
    if service_account_path and os.path.exists(service_account_path):
        cred = credentials.Certificate(service_account_path)
        initialize_app(cred, {
            'databaseURL': 'https://isa2025-f3173-default-rtdb.asia-southeast1.firebasedatabase.app/'
        })
        with open("firebase_admin_initialized.txt", "w") as f:
            f.write("Firebase Admin Initialized")
    else:
        st.error("Service account JSON file not found. Set the FIREBASE_ADMIN_JSON environment variable.")

# Function to save data to Firebase Realtime Database
def save_to_firebase(user_data):
    try:
        # Push the data to the Firebase database
        ref = db.reference('/registrations')
        ref.push(user_data)
        st.success("Registration details successfully saved to Firebase!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit app
def main():
    st.title("ISA Hackathon Registration")
    
    # Registration form
    with st.form(key='registration_form'):
        # Collect user details
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        contact = st.text_input("Contact Number")
        
        # Upload GPay screenshot
        screenshot = st.file_uploader("Upload your GPay screenshot", type=["jpg", "jpeg", "png"])
        
        # Terms and Conditions
        agree = st.checkbox("I agree to the terms and conditions")
        
        # Submit button
        submit_button = st.form_submit_button(label="Submit")
        
        if submit_button:
            if name and email and contact and screenshot and agree:
                # Prepare user data
                user_data = {
                    "Name": name,
                    "Email": email,
                    "Contact": contact,
                    "Screenshot": screenshot.name,
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                # Save the data to Firebase
                save_to_firebase(user_data)
            else:
                st.error("Please fill all the fields and agree to the terms and conditions.")

if __name__ == "__main__":
    main()
