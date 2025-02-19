import streamlit as st

def app():
    st.title("Thank You to Our Sponsor!")

    # Display sponsor logo
    st.image("https://github.com/Keerthivasan-11/ISA/blob/main/Placaka.png", 
             width=300, 
             caption="Placka Instruments - Our T-Shirt Sponsor")

    # Sponsor message
    st.markdown("""
        ## A Special Thanks to Placka Instruments!
        We extend our heartfelt gratitude to **Placka Instruments** for their generous sponsorship 
        of T-shirts for our event. Your support helps us create a more engaging and professional 
        experience for all participants.
    """)

    # Sponsor website link
    st.markdown("""
        👉 Visit [Placka Instruments](https://www.plackainstruments.com/) to learn more about their products and services.
    """, unsafe_allow_html=True)
