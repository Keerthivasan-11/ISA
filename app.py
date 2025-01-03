import streamlit as st
import pandas as pd
import os
from PIL import Image

# Page Title
st.title("ISA Hackathon 2025 Registration")

# Registration Form
st.header("Register for the Hackathon")
with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    contact = st.text_input("Contact Number")
    team_name = st.text_input("Team Name (Optional)")
    agree = st.checkbox("I agree to the terms and conditions")
    
    # Upload GPay Screenshot
    uploaded_file = st.file_uploader("Upload GPay Screenshot", type=["jpg", "jpeg", "png"])

    # Submit Button
    submitted = st.form_submit_button("Submit")

# Handle form submission
if submitted:
    if agree:
        # Check if the CSV file exists
        file_path = "registrations.csv"
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
        else:
            # Create a new dataframe with headers if the file does not exist
            df = pd.DataFrame(columns=["Name", "Email", "Contact", "Team Name"])

        # Add new data
        new_data = {"Name": [name], "Email": [email], "Contact": [contact], "Team Name": [team_name]}
        new_df = pd.DataFrame(new_data)
        df = pd.concat([df, new_df], ignore_index=True)

        # Save the updated data to CSV
        df.to_csv(file_path, index=False)
        st.success("Thank you for registering!")

        # If an image is uploaded, display it
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded GPay Screenshot", use_column_width=True)
    else:
        st.error("You must agree to the terms and conditions to register.")
