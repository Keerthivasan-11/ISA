import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import json

# Define the JSON credentials directly in the code
service_account_info = {
  "type": "service_account",
  "project_id": "static-destiny-446816-f4",
  "private_key_id": "88fdbed901c2dd0cb1f9729de6fa4db4405829b2",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCbHTh5cY6tcOzh\ntrR02wqIRLtsCwrCppttf3T9qpB6YsCKAVSaTNFGMFP1+dHwRhjzX5/SI5C0udh7\nLac1hZXJoAGTFw40VKnBX9SzW/ytLH2zgFoQtdEUcmg0DCvF+u8s3MWWPK//EY1s\n9thkVJnVhMaINtSpVulrx8tT0oJPGaSnEbX8j9KhPMRLj6TNGqGIUB0RbkUi451/\nRP759EgySu2G/njvKZ3vJ300W3n+A4SYuXSMIu2Yv5jGP8MkPYsI0G2hNz0hzUFh\n4y0tasKJ31UsMX2ydGuH/rE0SYpeHtmQG5zcL3+rrtchF4HySnyCyt6Ww5IvL9Tx\nh1ntd+79AgMBAAECggEAIcZr0uPTZ7hAWEimhBBi+3eN4PGJkwdgrifT8101rvR8\nTMCL6bpC0lf5HEUcvcchrTK78++bFYMnHHE9KMYQ7tGIrjzVsrbhrNHfWHu16gZX\nS6Pt2JgiceOUhYrF6Eri0/+xhWxq/S0XAKxCQ5x5T7kk2qmnxkS+uGGNiE+84JiT\nzFJ42JV3y3CkQb0UEjHajgCnEa9uxX+7Ub5Gv9p8TSEnektE0Zdsd3SW4U588XTy\nqCecDjTJKTic5KCqCE7mGc6hk8kQs31eeceSJ5Xa4KuGZMUcY7CzclPzgJchYWyh\nmFiFO07iOYlr3ih8IuXbX0vwXT3JoTtdpb1ypFq5aQKBgQDJoNGoWhi2xoeDBAYo\nQJozMI62FqW1hBHnIGPS9zNtLN3lAB+wOR8tq0iB98m0r9zuC1u6i/tTNxR2xzAj\n1x7p3xlnbXb0LN68DNBtCtEyqFI7PCi3Zh27IMZ+qcN6SGy1Y99jqvwkOcwNmhwK\ne1sI/VA4zSm8NHsKE6gBLMoaCQKBgQDE8VrbMUVXsWK+XBXLTEjOLYEiDOE6fp0H\nDt9ef7leF++KaL7b2t7bsEO0iOP7i80vWXCvTG51CTe+kTiux2sbXx3OQ5kYuJ4+\nF5uDS5iCPf6oHZ5GPcCUGm6B8LMi2lauahROiw1387hFwsSe3bubIP6soxrM1+Pv\nVxHH7416VQKBgBd3zG9X7UB44xTwxvawbkI/CJ1RDYCPGrZYIsZPV4EBk+IvnYCZ\nZXOfWBUojiWlwoVCdS7FVD9fTdZ1YLkLNOHrwb00FIBfKJ2isC/A7pCC3u9eFS8j\nh5pcOj5L7CCzhVOniDzFjgt5XrLGmTTvHq1xLoEuAAmT4i5OE2PvnqZhAoGBAIdx\nthqpeBcnV9GzYwm+HRQvF3Bji0K/cR85i0VicgnUTFnUT+7ESCCuyOGQg7qsGyFF\nUco9tnmnLT9SgLkzTOY2NDl3JANsdOgfNETH6Msp98mHFSMZtSgmRXn4IDsIDjVF\nn1GlME4ev8y6dp8Lv8qgloYEZpoaoBgquX/XsGVBAoGAYUc8MsBIz9hQs+eK887W\nu1gyky9UD3QxeGJHe0DevwHxvN2PLbVmsGkCa0iyVsI/M9TKUDIE9jBJkXAafyW6\nfmzgACAKsA1J+3BZIy0q6BgGqxEk/piXH+xPX5zEIXtszBLF9s46PCPaqQVbTRfk\nI4hhwTXz6LF/odJbXwxOSGI=\n-----END PRIVATE KEY-----\n",
  "client_email": "keerthivasan@static-destiny-446816-f4.iam.gserviceaccount.com",
  "client_id": "101328845318906344415",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/keerthivasan%40static-destiny-446816-f4.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# Authenticate using the provided credentials
def authenticate_google_sheets():
    credentials = Credentials.from_service_account_info(service_account_info)
    client = gspread.authorize(credentials)
    return client

# The function to save data to Google Sheets
def save_to_google_sheet(data):
    client = authenticate_google_sheets()
    # Add your sheet name here
    sheet = client.open('YourSheetName').sheet1
    sheet.append_row(data)

# Main function to handle Streamlit interface and data collection
def main():
    st.title('Person Registration')
    
    # Collect user input
    name = st.text_input('Name')
    age = st.number_input('Age', min_value=1, max_value=120)
    email = st.text_input('Email')
    
    data = [name, age, email]
    
    if st.button('Save to Google Sheet'):
        save_to_google_sheet(data)
        st.success('Data saved successfully!')

if __name__ == '__main__':
    main()
