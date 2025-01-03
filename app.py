import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Define the directory to save the data
data_directory = "data"
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

# Function to save user data to CSV
def save_to_csv(user_data):
    csv_file_path = os.path.join(data_directory, "registrations.csv")
    df = pd.DataFrame([user_data])
    if os.path.exists(csv_file_path):
        df.to_csv(csv_file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_file_path, mode='w', header=True, index=False)

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
                # Save the registration details if everything is correct
                user_data = {
                    "Name": name,
                    "Email": email,
                    "Contact": contact,
                    "Screenshot": screenshot.name,
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                save_to_csv(user_data)
                
                # Display success message
                st.success("Thank you for registering!")
                
                # Optionally, display uploaded file
                st.image(screenshot, caption="Uploaded GPay Screenshot", use_column_width=True)
            else:
                st.error("Please fill all the fields and agree to the terms and conditions.")

if __name__ == "__main__":
    main()
