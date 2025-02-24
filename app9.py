import streamlit as st

def app():
    # Page title
    st.title("🙏 Sponsorship Appreciation 🙏")

    # Sponsor 1: Placka Instruments
    sponsor1_name = "Placka Instruments India Pvt Ltd"
    sponsor1_website = "https://www.plackainstruments.com/"
    sponsor1_logo = "https://github.com/Keerthivasan-11/ISA/blob/main/Placaka.png?raw=true"
    sponsor1_address = """
    No-5, Ramamoorthy Street, Nehru Nagar, Chromepet, Chennai - 600 044, India.<br>
    📞 Phone: +91-44-22231559, 22234562, 22230187 <br>
    📠 Fax: +91-44-22236984 <br>
    📧 Email: <a href='mailto:sales@plackainstruments.com'>sales@plackainstruments.com</a>, 
    <a href='mailto:plackainstruments@yahoo.com'>plackainstruments@yahoo.com</a>
    """
    
    # Sponsor 2: Base Automation
    sponsor2_name = "Base Automation"
    sponsor2_website = "https://baseautomation.co.in/"
    sponsor2_logo = "https://github.com/Keerthivasan-11/ISA/blob/main/Website-Logo-with-CSIA.png?raw=true"
    sponsor2_address = """
    276, 2nd Main Road, Nehru Nagar, Kottivakkam, OMR, Chennai – 600096, India.<br>
    📞 Phone: +91 73388 97775 <br>
    📧 Email: <a href='mailto:consult@batpl.com'>consult@batpl.com</a>
    """
    sponsor2_contribution = "₹10,000 💰 (for decoration work at ISA Hackathon)"

    # Display Sponsor 1 (Placka Instruments)
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h2 style="color: #1f4e79;">Special Thanks to Our Sponsor</h2>
            <img src="{sponsor1_logo}" width="300" alt="Placka Instruments Logo">
            <p style="font-size: 18px; color: #333;">
                We extend our heartfelt gratitude to <strong>{sponsor1_name}</strong> 
                for their generous support and contributions to the ISA MIT Student Chapter.
            </p>
            <p style="font-size: 16px; color: #555;">{sponsor1_address}</p>
            <p>
                <a href="{sponsor1_website}" style="font-size: 18px; color: #FFA500;">
                    Visit Placka Instruments
                </a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # T-Shirt Acknowledgment
    st.markdown(
        """
        <div style="text-align: center; margin-top: 30px;">
            <h3 style="color: #1f4e79;">Special Thanks for T-Shirt Sponsorship</h3>
            <p style="font-size: 16px; color: #333;">
                We sincerely thank <strong>Placka Instruments</strong> for arranging high-quality 
                T-shirts and ensuring timely delivery for our event.
            </p>
            <p>👕🎉</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Display Sponsor 2 (Base Automation)
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: 50px;">
            <h2 style="color: #1f4e79;">A Huge Thanks to Base Automation</h2>
            <img src="{sponsor2_logo}" width="300" alt="Base Automation Logo">
            <p style="font-size: 18px; color: #333;">
                <strong>{sponsor2_name}</strong> has generously contributed <strong>{sponsor2_contribution}</strong>
                for decoration work at the ISA Hackathon. We deeply appreciate their support!
            </p>
            <p style="font-size: 16px; color: #555;">{sponsor2_address}</p>
            <p>
                <a href="{sponsor2_website}" style="font-size: 18px; color: #FFA500;">
                    Visit Base Automation
                </a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()
