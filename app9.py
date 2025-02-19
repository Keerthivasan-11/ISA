import streamlit as st

def app():
    # Page title
    st.title("🙏 Sponsorship Appreciation 🙏")

    # Sponsor details
    sponsor_name = "Placka Instruments"
    sponsor_website = "https://www.plackainstruments.com/"
    sponsor_logo = "https://github.com/Keerthivasan-11/ISA/blob/main/Placaka.png?raw=true"

    # Center-aligned sponsorship message
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h2 style="color: #1f4e79;">Special Thanks to Our Sponsor</h2>
            <img src="{sponsor_logo}" width="300" alt="Placka Instruments Logo">
            <p style="font-size: 18px; color: #333;">
                We extend our heartfelt gratitude to <strong>{sponsor_name}</strong> 
                for their generous support and contributions to the ISA MIT Student Chapter.
            </p>
            <a href="{sponsor_website}" target="_blank" style="font-size: 18px; color: #FFA500;">
                Visit Placka Instruments
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
