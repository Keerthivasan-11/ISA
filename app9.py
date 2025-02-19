import streamlit as st

def app():
    # Page title
    st.title("🙏 Sponsorship Appreciation 🙏")

    # Sponsor details
    sponsor_name = "Placka Instruments India Pvt Ltd"
    sponsor_website = "https://www.plackainstruments.com/"
    sponsor_logo = "https://github.com/Keerthivasan-11/ISA/blob/main/Placaka.png?raw=true"

    sponsor_address = """
        No-5, Ramamoorthy Street, Nehru Nagar, <br>
        Chromepet, Chennai - 600 044, India.
    """
    sponsor_phone = "📞 91-44-22231559, 22234562, 22230187"
    sponsor_fax = "📠 91-44-22236984"
    sponsor_email = """
        ✉ sales@plackainstruments.com <br>
        ✉ plackainstruments@yahoo.com
    """

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
            <p style="font-size: 16px; color: #333;">
                {sponsor_address} <br>
                {sponsor_phone} <br>
                {sponsor_fax} <br>
                {sponsor_email}
            </p>
            <p>
                <a href="{sponsor_website}" style="font-size: 18px; color: #FFA500;">
                    Visit Placka Instruments
                </a>
            </p>
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
            <p>
                <a href="{tshirt_provider_website}" style="font-size: 18px; color: #FFA500;">
                    Visit Root5
                </a>
            </p>
            <p style="font-size: 16px; color: #333;">{tshirt_provider_contact}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()
