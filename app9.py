import streamlit as st

def app():
    # Page title
    st.title("🙏 Sponsorship Appreciation 🙏")

    # Sponsor details
    sponsor_name = "Placka Instruments"
    sponsor_website = "https://www.plackainstruments.com/"
    sponsor_logo = "https://github.com/Keerthivasan-11/ISA/blob/main/Placaka.png?raw=true"

    tshirt_provider_name = "Root5"
    tshirt_provider_website = "https://www.root5.in/"
    tshirt_provider_logo = "https://github.com/Keerthivasan-11/ISA/blob/main/Capture.JPG?raw=true"
    tshirt_provider_contact = "📞 8925379459"

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
        <br>
        <div style="text-align: center;">
            <h3 style="color: #1f4e79;">Acknowledgment for T-Shirt Order</h3>
            <img src="{tshirt_provider_logo}" width="300" alt="Root5 Logo">
            <p style="font-size: 18px; color: #333;">
                A special thanks to <strong>{tshirt_provider_name}</strong> for fulfilling our 
                T-shirt order placed by Placka Instruments and delivering high-quality T-shirts 
                on time for the event.
            </p>
            <a href="{tshirt_provider_website}" target="_blank" style="font-size: 18px; color: #FFA500;">
                Visit Root5
            </a>
            <p style="font-size: 16px; color: #333;">{tshirt_provider_contact}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()
