import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
import app1
import app2
import app3
import app4
import app5
import app6
import app7
import app8
import app9  # Import sponsorship page

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(
    page_title="ISA MIT Student Chapter",
    page_icon="📘",
    layout="wide"
)

# CSS to style the sidebar and highlight the arrow
st.markdown("""
    <style>
        /* Hide Streamlit Branding */
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Sidebar styling */
        .css-1lcbmhc {
            background-color: #1f4e79;
            color: white;
            padding: 15px;
            font-size: 16px;
        }

        /* Sidebar options */
        .css-1j3uqpy {
            color: white !important;
            font-size: 18px !important;
        }

        .css-1j3uqpy:hover {
            color: #FFA500 !important;
        }

        /* Sidebar arrow customization */
        .css-1lcbmhc .stSidebarIcon {
            font-size: 36px !important;
            color: #FFA500 !important;
        }

        .css-1lcbmhc .stSidebarIcon:hover {
            font-size: 40px !important;
            color: #FF6347 !important;
        }

        /* Mobile adjustments */
        @media (max-width: 768px) {
            .css-1lcbmhc .stSidebarIcon {
                font-size: 40px !important;
            }
            .css-1j3uqpy {
                font-size: 16px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    selected_option = option_menu(
        menu_title="ISA MIT Student Chapter",
        options=[
            "Home", 
            "Laboratory Facilities", 
            "Sponsorship",  # Sponsorship page
            "2024 Events", 
            "International Society of Automation Officer", 
            "Registration form", 
            "Gform registration", 
            "About", 
            "Contact"
        ],
        icons=[
            "house-fill", 
            "calendar-event-fill", 
            "person-plus-fill",  # Sponsorship icon
            "book-fill", 
            "info-circle-fill", 
            "envelope-fill"
        ],
        menu_icon="gear-fill",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#1f4e79"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"color": "white", "font-size": "18px", "--hover-color": "#FFA500"},
            "nav-link-selected": {"background-color": "#FFA500"},
        }
    )

# Page Logic
if selected_option == "Home":
    app2.app()
elif selected_option == "Registration form":
    app1.app()
elif selected_option == "Gform registration":
    app3.app()
elif selected_option == "Laboratory Facilities":
    app4.app()
elif selected_option == "Sponsorship":  
    app9.app()  # Calls app9 when Sponsorship is selected
elif selected_option == "2024 Events":
    app5.app()
elif selected_option == "International Society of Automation Officer":
    app8.app()
elif selected_option == "About":
    app6.app()
elif selected_option == "Contact":
    app7.app()
