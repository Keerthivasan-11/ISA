import streamlit as st
import pandas as pd

# Page Title
st.title("ISA Hackathon 2025 Registration")

# Registration Form Section
st.header("Register for the Hackathon")
with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    contact = st.text_input("Contact Number")
    team_name = st.text_input("Team Name (Optional)")
    agree = st.checkbox("I agree to the terms and conditions")

    # Submit Button
    submitted = st.form_submit_button("Submit")

if submitted:
    if agree:
        # Save registration data to CSV
        data = {"Name": [name], "Email": [email], "Contact": [contact], "Team Name": [team_name]}
        df = pd.DataFrame(data)
        df.to_csv("registrations.csv", mode="a", header=False, index=False)
        st.success("Thank you for registering!")
    else:
        st.error("You must agree to the terms and conditions to register.")

# Admin Section
st.header("View Registered Participants")
try:
    # Read registration data from CSV and display it
    df = pd.read_csv("registrations.csv", header=None, names=["Name", "Email", "Contact", "Team Name"])
    st.dataframe(df)
except FileNotFoundError:
    st.error("No registration data found yet.")
