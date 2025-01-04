import os
import streamlit as st
import firebase_admin
from firebase_admin import credentials, initialize_app, db
from datetime import datetime

# Firebase credentials JSON data (directly included here)
firebase_credentials = {
    "type": "service_account",
    "project_id": "isa2025-f3173",
    "private_key_id": "89916782aefc60e6941e85a127418a9598ecda0a",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCiOoRJXHgFXyAq\nHTopeRkBIqJ2iBGgJb0eshJRCElqL6dKZc0hrMvEohJjL2nJPBijCZ8ZpY4OYszA\nsHuWWjYHm8vQd5oc/ZnPfnzBS52YTy1f+dfXwntsn7P6dESdzPlmg4sxPYDoddR5\nfWrDG8yI8xuQLfvG6zFiVh6EQht/9BoNspnziih3KGIE23BHxDTSlMcf84TAYBc8\nICLszx7bpWiBGUFCrgTJVy0HaCyH3sf2zxUULCAcgPJAbNCozV9dX2kdefoF0eZh\nOUDIuMu6w6kv/VTs//eOmftgaabGILQ8FR3AhU9PjTn5c8JIRAHHXyeP4XFTCxj2\nu1H1ys2jAgMBAAECggEAOWzKT+eeCpS6H346DN0zZy354UhYKN7C+58gEbQDvMVC\ni/jOLInslV2jcZ2ibhvKQsgQm/T4/Imnndu626VyM65H7rKviGySqhrFkWyxS+1X\nC/62E0diBjjf7huDAHLCo7GTr2nsfBzdieXFyWvJMn8PtjE4yxiM4hjG850s+9T9\nroHNbWMzgc/fgZz0y/Q0Qc3mqrXeATjZkE971yU+GzlClHVMXnKv7R/nKTOYy/P1\nI4EY8XXpEjYtJsSUuw83yQctrC1KOVGS1xY49zkBlin+7aLVm1tixXqGufNcBe0X\nY9OTnu6BwRGknU9gtxYJelNO47RFpA9MyEWtsYPKiQKBgQDNKYLa5Ho7qgsYWS7D\n1K9Yj2LsKW6qfkwt3UJCtjiH7whTUOHAQRQu2bDrqyyMqDXiuQHoFVK8ytljSGg+\nEYUc1IAdhjB5WmdntyQ5NXuWnz4i5P3zuyAZg2TXRIPEZJMx/5jvMzodIswmivkz\ndmPS3Zg/zv4RJKi+gtr4lW7TSwKBgQDKbYI39VZ2kIFB855vB1QLrNPRuEIMc2J3\nz6VYrAjwYaeEyldaeWHALULFFhW39+3JhXvGdLCsWqPUgJCXvMC6MpakkcDdrEun\nuX36r8gtABIUMATmbRhOMitpSIo4gfNqUBhRxUpZiVoG98MemnLbWzAj20WE2PS0\nLz5PBfQgCQKBgBaeIe/xykvzlh+MDWzHcMFJpXU1qB6hp9JSlzB1mEvcHUXaH9kr\nE4eKtkd06odjL/WbwcsNNr7behXI8L0O/2bLQoh+t69ZORclCJhJ/iL/0UDVj+2j\nzokhhCd7RS+MivGzJPAR7LEzmeAR6CE1RxIDHfrC3h2TtgqysGNBTiN7AoGALI1d\nk6NTnFTBnhpYTGd4f/lRxV6gas0aZvQ0mAeFECLuE7PU9fyxHvLXNzldHlha5XeT\nfmJAYC6y0BpbuIm6gUCRFzddE2zQWeHhcEMv83eIgxjueyiXqN4x38IvabBwOn3W\nXGjnrD0mq1Hsh9fGX7D6L2obKtn1QZMES7ArwsECgYBSBCQzfJtGZTsd4GQHoQqZ\n50PiNT/UjKaPYXnZDMTMlIg/4gknEEL6jVZ6tWpjYIiqWlRAk1UFPadTqWR6XpuD\n56BOpWxn8gOAOu1ETFLlY2G4zRbBfshHjxa8NFHYWtrEsDCZgxNXtLB2UX1wGruy\nczQxjdlCv7jpa2HOPqDr3w==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-5zx9w@isa2025-f3173.iam.gserviceaccount.com",
    "client_id": "106456162339754757984",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-5zx9w%40isa2025-f3173.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# Function to initialize Firebase app
def initialize_firebase():
    try:
        # Initialize Firebase with the provided credentials
        cred = credentials.Certificate(firebase_credentials)
        initialize_app(cred, {
            'databaseURL': 'https://isa2025-f3173-default-rtdb.asia-southeast1.firebasedatabase.app/'
        })
        st.success("Firebase Admin SDK Initialized Successfully!")
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
                st.error("Please fill in all the fields and agree to the terms and conditions.")

    # Button to fetch and display data
    if st.button("Show Registrations"):
        fetch_from_firebase()

if __name__ == "__main__":
    main()
