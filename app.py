import streamlit as st
import pandas as pd
import os

# Page Title
st.title("ISA Hackathon 2025")

# Navigation Buttons
st.write("Welcome to the ISA Hackathon!")
if st.button("Register for the Hackathon"):
    # Registration Form Section
    st.header("Register for the Hackathon")
    with st.form("registration_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        contact = st.text_input("Contact Number")
        team_name = st.text_input("Team Name (Optional)")
        gpay_screenshot = st.file_uploader("Upload GPay Screenshot", type=["png", "jpg", "jpeg"])
        agree = st.checkbox("I agree to the terms and conditions")

        # Submit Button
        submitted = st.form_submit_button("Submit")

    if submitted:
        if agree:
            if gpay_screenshot is not None:
                # Save the screenshot locally in an "uploads" folder
                upload_dir = "uploads"
                os.makedirs(upload_dir, exist_ok=True)
                file_path = os.path.join(upload_dir, gpay_screenshot.name)
                with open(file_path, "wb") as f:
                    f.write(gpay_screenshot.getbuffer())
                
                # Save registration data to CSV
                data = {
                    "Name": [name],
                    "Email": [email],
                    "Contact": [contact],
                    "Team Name": [team_name],
                    "GPay Screenshot": [file_path]
                }
                df = pd.DataFrame(data)
                df.to_csv("registrations.csv", mode="a", header=False, index=False)
                st.success("Thank you for registering!")
            else:
                st.error("Please upload your GPay screenshot.")
        else:
            st.error("You must agree to the terms and conditions to register.")

# Admin Section (Hidden with Password)
with st.expander("Admin Access (Click to Expand)"):
    password = st.text_input("Enter Admin Password", type="password")
    if password == "admin123":  # Replace with a secure password
        st.header("View Registered Participants")
        try:
            # Read registration data from CSV and display it
            df = pd.read_csv("registrations.csv", header=None, names=["Name", "Email", "Contact", "Team Name", "GPay Screenshot"])
            st.dataframe(df)
        except FileNotFoundError:
            st.error("No registration data found yet.")
    elif password:
        st.error("Incorrect password!")
