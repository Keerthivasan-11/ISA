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

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(
    page_title="ISA MIT Student Chapter",
    page_icon="📘",
    layout="wide"
)

# CSS to hide Streamlit branding, GitHub symbol, and extra elements
st.markdown("""
    <style>
        /* Hide Streamlit Branding */
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Hide GitHub symbol and other unnecessary icons */
        .stDeployButton, .css-1rs6os {display: none !important;}
        
        /* Custom styling for sidebar */
        .sidebar .sidebar-content {
            background-color: #1f4e79;  /* Sidebar color */
            color: white;
            padding: 15px;
            font-size: 16px;
        }
        
        .sidebar .sidebar-header {
            font-size: 24px;
            font-weight: bold;
            color: white;
        }
        
        /* Scrollbar styling for the sidebar */
        .css-1d391kg {
            background-color: #1f4e79;
        }

        /* Custom button styling */
        .stButton>button {
            background-color: #02ab21;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
        }

        .stButton>button:hover {
            background-color: #1f4e79;
        }
        
        /* Custom heading style */
        h1, h2, h3 {
            color: #1f4e79;
            font-weight: bold;
        }

        /* Custom font styling */
        body {
            font-family: 'Arial', sans-serif;
        }

        /* Highlight the arrow for sidebar in mobile */
        .css-18ni7ap {
            color: #FFA500 !important;  /* Change arrow color to orange */
            font-size: 24px !important;  /* Increase arrow size */
            animation: pulse 2s infinite;  /* Add pulsing animation */
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
    </style>
""", unsafe_allow_html=True)

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

# Scrolling Image and Text
def display_scrolling_content():
    st.markdown(""" 
    <style>
        .scrolling-container {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            overflow: hidden;
        }
        .scrolling-content {
            display: flex;
            animation: scroll 10s linear infinite;
            align-items: center;
        }
        .scrolling-content img {
            height: 60px;  /* Adjust image size to match text */
            margin-right: 15px;  /* Space between image and text */
        }
        .scrolling-content span {
            font-size: 32px;  /* Adjust font size to match image height */
            font-weight: bold;
            color: #1f4e79;  /* Change text color as per requirement */
            line-height: 60px;  /* Align text vertically with image */
        }
        @keyframes scroll {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
    </style>
    <div class="scrolling-container">
        <div class="scrolling-content">
            <img src="https://github.com/Keerthivasan-11/ISA/blob/main/isa%20image.png?raw=true" alt="ISA Image">
            <span> & Department of Instrumentation Engineering</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    selected_option = option_menu(
        menu_title="ISA MIT Student Chapter",
        options=["Home","Laboratory Facilities", "2024 Events","International Society of Automation Officer", "Registration form", "Gform registration", "About", "Contact"],
        icons=["house-fill", "calendar-event-fill", "person-plus-fill", "book-fill", "info-circle-fill", "envelope-fill"],
        menu_icon="gear-fill",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#1f4e79"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"color": "white", "font-size": "18px", "margin": "0px", "--hover-color": "#FFA500"},
            "nav-link-selected": {"background-color": "#FFA500"},  # Highlight selected option in orange
        }
    )

# Page Logic
if selected_option == "Home":
    # Display scrolling image and text
    display_scrolling_content()
    app2.app()
elif selected_option == "Registration form":
    app1.app()
elif selected_option == "Gform registration":
    app3.app()
elif selected_option == "Laboratory Facilities":
    app4.app()
elif selected_option == "2024 Events":
    app5.app()
elif selected_option=="International Society of Automation Officer":
    app8.app()
    
elif selected_option == "About":
    app6.app()
elif selected_option == "Contact":
    app7.app()
