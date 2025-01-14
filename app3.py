import streamlit as st

def app():
    st.title("🌟 Event Registration and Payment 🏆")
    
    st.markdown("""
        ### 📌 **Important Instructions**
        - Make sure to fill **both the Google Form** and this **Website Form** to complete your registration.
        - After completing the registration, use the payment details to proceed with payment.

        ### 📝 **Google Form Registration:**
        - Please fill out the registration form using the link below:

        [Fill the Registration Form](https://docs.google.com/forms/d/e/1FAIpQLSeVWmnEmcbFz2rE68iC9oUWcf4qdZJFyivGmBsuCr2rAMmvkw/viewform)

    """)
    
    # Display the QR code image for GPay payment
    qr_code_url = "https://github.com/Keerthivasan-11/ISA/blob/main/qrcode_159208919_9c425f9aad044cff32e6661c000bc9cf.png?raw=true"
    st.image(qr_code_url, caption="Scan to Pay to fill gform", width=500)

    st.markdown("""
        ### 🎉 Thank you for registering! 🎉
        - Please ensure you complete all required steps.
    """)

# Running the Streamlit app
if __name__ == "__main__":
    app()
