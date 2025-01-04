import os
import streamlit as st
import firebase_admin
from firebase_admin import credentials, initialize_app, db
from datetime import datetime

# Firebase credentials JSON data (directly included here, replace with your own)
firebase_credentials = {
    "type": "service_account",
    "project_id": "your-project-id",  # Replace with your Firebase Project ID
    "private_key_id": "your-private-key-id",  # Replace with your private key ID
    "private_key": "your-private-key",  # Replace with the actual private key
    "client_email": "your-client-email@firebase.iam.gserviceaccount.com",  # Replace with your client email
    "client_id": "your-client-id",  # Replace with your client ID
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "your-client-cert-url",  # Replace with your client cert URL
    "universe_domain": "googleapis.com"
}

# Function to initialize Firebase app
def initialize_firebase():
    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate(firebase_credentials)
            initialize_app(cred, {
                'databaseURL': 'https://your-database-url.firebaseio.com'  # Replace with your Firebase Realtime Database URL
            })
            st.success("Firebase Admin SDK Initialized Successfully!")
        else:
            st.info("Firebase Admin SDK is already initialized.")
    except Exception as e:
        st.error(f"Error initializing Firebase: {e}")

# Function to save data to Firebase Realtime Database
def save_to_firebase(user_data):
    try:
        # Push the data to the Firebase database
        ref = db.reference('/registrations')
        ref.push(user_data)
        st.success("Registration details successfully saved to Firebase!")
    except Exception as e:
        st.error(f"An error occurred while saving data: {e}")

# Function to fetch and display data from Firebase Realtime Database
def fetch_from_firebase():
    try:
        # Reference the registrations node
        ref = db.reference('/registrations')
        data = ref.get()
        
        # Display data in the Streamlit app
        if data:
            st.subheader("Registered Details:")
            for key, value in data.items():
                st.write(f"Name: {value['Name']}")
                st.write(f"Email: {value['Email']}")
                st.write(f"Contact: {value['Contact']}")
                st.write(f"Timestamp: {value['Timestamp']}")
                st.write("---")
        else:
            st.warning("No registrations found.")
    except Exception as e:
        st.error(f"An error occurred while fetching data: {e}")

# Streamlit app
def main():
    st.title("ISA Hackathon Registration")

    # Initialize Firebase
    initialize_firebase()

    # Registration form
    with st.form(key='registration_form'):
        # Collect user details
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        contact = st.text_input("Contact Number")
        
        # Terms and Conditions
        agree = st.checkbox("I agree to the terms and conditions")
        
        # Submit button
        submit_button = st.form_submit_button(label="Submit")
        
        if submit_button:
            if name and email and contact and agree:
                # Prepare user data
                user_data = {
                    "Name": name,
                    "Email": email,
                    "Contact": contact,
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                # Save the data to Firebase
                save_to_firebase(user_data)
            else:
                st.error("Please fill in all the fields and agree to the terms and conditions.")

    # Button to fetch and display data
    if st.button("Show Registrations"):
        fetch_from_firebase()

if __name__ == "__main__":
    main()
