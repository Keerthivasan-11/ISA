import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin.firestore import SERVER_TIMESTAMP

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate('https://github.com/Keerthivasan-11/ISA/blob/dc5a0beec0fa6ed54988c4c9bb37a5193e7e70f6/isa2025-f3173-firebase-adminsdk-5zx9w-323e82754a.json')
    firebase_admin.initialize_app(cred)

# Create Firestore client
db = firestore.client()

# Streamlit UI to input data
st.title("Enter User Details")

with st.form(key='user_form'):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120)
    city = st.text_input("City")
    
    submit_button = st.form_submit_button("Submit")
    
    if submit_button:
        # Use Firebase's server timestamp instead of local time
        data = {
            "name": name,
            "age": age,
            "city": city,
            "timestamp": SERVER_TIMESTAMP  # This is a special Firestore field for server timestamp
        }
        
        try:
            doc_ref = db.collection('users').add(data)
            st.success(f"Data saved successfully with ID: {doc_ref.id}")
        except Exception as e:
            st.error(f"An error occurred while saving data: {e}")
            print(f"Error: {e}")
