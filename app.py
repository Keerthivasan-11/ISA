import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Directly using the credentials from the TOML file you provided

credentials_dict = {
    "type": "service_account",
    "project_id": "isa-registration",
    "private_key_id": "0360586fc02928fd242cbb038598e1d7227d6d88",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC+EVvzJmorl1Bn\nHODQzZyqiKOLCwUy9zet9ZyAcfDhdYpTzqYaKCTEHee41XX4obd5iWNocGy/3jdz\naN2cQAGImc3bps3dtzm3VBfTBAnCvxCtGYMQozqLwoLdRiXCAC7w7N5OtY24Kh4f\neT+P9bk/xnJZF9hrHtnsiWzeHnox1Pzkd0+5+5jD7glA0O0hkG2lf2PiaJBZxtXo\ndyf1syl+YNXX2UxVipob0wvjPXTSoU50W3vEFFJBMhR4nmsXS8HCts5MQt7sPF8m\nmxvPYuPpOL5qzGJ9S6sghX33u1tfZFBO8fVDlRIMc3pEbXCcvKtBj05ud4OMiJOg\nVmxPCUR9AgMBAAECggEAAy0ol3tunkxg0lxT8IFjKyFt9EKqo1Oo2U4nv6jH0QjF\nF0n2kizWEnX6e6cLmexf89bFM8dfNeSpkhLwUy5pqCYD3/YdbiVkAEmWPVdNr3TA\ne1gYDeTgc1n8lGSZ+HBG2I1o2LFljSydBMMiug3t+uAe5JjGq+Gf3DleuaaSPbdt\nWZzuTh9s67Vb9nsVpT3wSko8jQ4xy0owScutWodO9imiLbTCYmJ3/tFTZ84MjJ3Z\n65GIKVT4p0rOvMCg9KpS4FDqEtCB4wYGOUeTCXxn6UBbnwiOTorwt6gIwmT5qsQY\nBF0wFHUqwUpXmFAnWZIBU2sULbj8cixw0zEAwXe0+QKBgQD1DmHVdE1ilRnuld6c\n/usWuu0LbXdmRE9azwzIuAKjCl1afhFk+IGV+Qz/vAarJknm5YV6lqDPTZhDrXw1\ns7nV88ysvSJ6rEm6xlvf3RnoCDEjb54sijfYXy/EWzN6Lkm8+E6bxThfFZ9IunJv\nRdk8YpW+G0I2SEHYZHMEvZsfRQKBgQDGjlHNAJ2qJLZhLT5dYcsjjsPvUu82eb5m\n04lOp/GBnCK5CUXs0pSktFECmQ3rABnOa7ptqcSfHRki/w3xEbJmmqo63bOZPgpO\n/bc+CTRhdZCa1M5qhGdhuJHBsSlglI5iYWaIYdjSaWVA/NzBte+riyTmNhHK+sro\n5gfDUQtn2QKBgQCrl5CF6NQvDXyFBchFYnK3DdjiQZpzr61pRsYK3l5qT92iedgw\nPZpvq16gy8ZXnY3t8hWPC147CnhuG1J4QAsGd5p/8kfsYiuWb0Lx9F4pjWLrD0NQ\nqNAF4FEQS1Q2X6cefTh99pFMc1V/lZ5/sAc3M0jrPycT33DL1zp6vVGbiQKBgEyC\n7xaWFCtKNlU///YwBv1OuEXyqWdOhoZNIW4D3VZaei7fWeimRM0rBsR/ghN6WHdo\nn9A+SRwfNF599jtc3GgZVVuVru1wMLy7m+710Q91JCHluxzkpInNe60tvYoP9MYI\nTmBjhA+guXnPdqnWl+J8nd1wHG8hMSuJ6JflFQYRAoGBAOVF92Ol4x9r/zejFKgb\nYso7KDkjTzGdXSgxtsmwUTDyLZ/jZ2rVR3FlndYOMNZLKjUmDTEMBWRXPWMePLEm\nGmqLtCuYM38PKVqT92QXJaXSXUD67uKbfe37doOCXcmsvSEQqtzJwJoHYc2p/N2Q\n4WcNr04N1SEwxqJQ8hHcy+54\n-----END PRIVATE KEY-----\n",
    "client_email": "keerthivasan@isa-registration.iam.gserviceaccount.com",
    "client_id": "105128829756602902365",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/keerthivasan%40isa-registration.iam.gserviceaccount.com"
}

# Authenticate using service account credentials
credentials = Credentials.from_service_account_info(credentials_dict, scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])

# Use gspread to access Google Sheets
client = gspread.authorize(credentials)

# Access the spreadsheet
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1UQZxEyP_JapwX5mu--9UtdcsrBJC3Fu4KbN9i7fd2sQ"
spreadsheet = client.open_by_url(spreadsheet_url)
worksheet = spreadsheet.worksheet("Sheet1")
try:
    # Access the spreadsheet
    spreadsheet = client.open_by_url(spreadsheet_url)
    worksheet = spreadsheet.worksheet("Registrations")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")

# Registration Form
st.title("ISA Hackathon Registration")
with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    team_name = st.text_input("Team Name")
    submitted = st.form_submit_button("Register")

    if submitted:
        if name and email and team_name:
            worksheet.append_row([name, email, team_name])
            st.success("You have successfully registered!")
        else:
            st.error("Please fill in all the fields.")
