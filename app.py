import os
import requests
import streamlit as st
import firebase_admin
from firebase_admin import credentials, initialize_app, db
from datetime import datetime

# Function to download the Firebase credentials file from GitHub
def download_firebase_credentials():
    try:
        # GitHub raw URL for your service account JSON file
        url = "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/isa2025-f3173-firebase-adminsdk-5zx9w-323e82754a.json"
        
        # Send a GET request to fetch the raw content of the JSON file
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        
        # Write the content to a local file
        with open("firebase_credentials.json", "wb") as file:
            file.write(response.content)
        
        st.success("Firebase credentials file downloaded successfully.")
    except Exception as e:
        st.error(f"Error downloading Firebase credentials: {e}")

# Function to initialize Firebase app
def initialize_firebase():
    try:
        # Check if the credentials file exists, if not, download it
        if not os.path.exists("firebase_credentials.json"):
            download_firebase_credentials()
        
        # Initialize Firebase with the downloaded credentials
        cred = credentials.Certificate("firebase_credentials.json")
        initialize_app(cred, {
            'databaseURL': 'https://isa2025-f3173-default-rtdb.asia-southeast1.firebasedatabase.app/'
        })
        st.success("Firebase Admin SDK Initialized Successfully!")
    except Exception as e:
        st.error(f"Error initializing Firebase: {e}")

# Function to save data to Firebase Realtime Database
def save_to_firebase(user_data):
    try:
        print(user_data)  # Debugging: Print user data to verify it's being passed correctly

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
    
    # Button to view registered details
    if st.button("View Registered Details"):
        fetch_from_firebase()

if __name__ == "__main__":
    main()
