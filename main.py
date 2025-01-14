import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
import app1
import app2
# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(
    page_title="ISA MIT Student Chapter",
    page_icon="📘",
    layout="wide"
)

# Google Analytics Integration
analytics_tag = os.getenv('analytics_tag')
if analytics_tag:
    st.markdown(
        f"""
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={analytics_tag}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{analytics_tag}');
        </script>
        """, unsafe_allow_html=True
    )

# Sidebar Navigation
with st.sidebar:
    selected_option = option_menu(
        menu_title="ISA MIT Student Chapter",
        options=["Home", "Events", "Registration form", "Resources", "About Us", "Contact"],
        icons=["house-fill", "calendar-event-fill", "person-plus-fill", "book-fill", "info-circle-fill", "envelope-fill"],
        menu_icon="gear-fill",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#1f4e79"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"color": "white", "font-size": "18px", "margin": "0px", "--hover-color": "#add8e6"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )

# Page Logic
if selected_option == "Home":
   app2.app()
elif selected_option == "Registration form":
   app1.app()
   st.markdown("### 🏦 **GPay QR Code for Payment**")
   gpay_qr_url = "https://github.com/Keerthivasan-11/ISA/blob/main/Gpay%20qr.jpeg?raw=true"
   st.image(gpay_qr_url, caption="Scan to Pay using GPay", use_column_width=True)

# elif selected_option == "Membership":
#     st.title("Membership Details")
#     st.write("Join the ISA MIT Student Chapter and be part of a vibrant community.")
# elif selected_option == "Resources":
#     st.title("Resources")
#     st.write("Access study materials, newsletters, and shared resources.")
# elif selected_option == "About Us":
#     st.title("About ISA MIT Student Chapter")
#     st.write("Learn about our mission, vision, and activities.")
elif selected_option == "Contact":
     st.title("Contact Us")
     st.write("Reach out to us for queries and suggestions.")
