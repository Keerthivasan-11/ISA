import streamlit as st

def app():
    # Page title
    st.title("🙏 Sponsorship Appreciation 🙏")

    # Sponsor details
    sponsor_name = "Placka Instruments India Pvt Ltd"
    sponsor_website = "https://www.plackainstruments.com/"
    sponsor_logo = "https://github.com/Keerthivasan-11/ISA/blob/main/Placaka.png?raw=true"

    # Supplier details
    tshirt_supplier_name = "Root5"
    tshirt_supplier_website = "https://www.root5.in/"
    tshirt_supplier_contact = "8925379459"
    tshirt_image = "https://github.com/Keerthivasan-11/ISA/blob/main/Capture.JPG?raw=true"

    # Sponsorship appreciation
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h2 style="color: #1f4e79;">Special Thanks to Our Sponsor</h2>
            <img src="{sponsor_logo}" width="300" alt="Placka Instruments Logo">
            <p style="font-size: 18px; color: #333;">
                We extend our heartfelt gratitude to <strong>{sponsor_name}</strong> 
                for their generous support and contributions to the ISA MIT Student Chapter.
            </p>
            <p>
                📍 <strong>Address:</strong> No-5, Ramamoorthy Street, Nehru Nagar, Chromepet, Chennai - 600 044, India.<br>
                📞 <strong>Phone:</strong> +91-44-22231559, 22234562, 22230187<br>
                📠 <strong>Fax:</strong> +91-44-22236984<br>
                📧 <strong>Email:</strong> <a href="mailto:sales@plackainstruments.com">sales@plackainstruments.com</a>, 
                <a href="mailto:plackainstruments@yahoo.com">plackainstruments@yahoo.com</a>
            </p>
            <p>
                <a href="{sponsor_website}" target="_blank" style="font-size: 18px; color: #FFA500;">
                    Visit Placka Instruments
                </a>
            </p>
            <hr>
            <h3 style="color: #1f4e79;">👏 Special Thanks to Root5 👕</h3>
            <img src="{tshirt_image}" width="300" alt="T-Shirt Order">
            <p style="font-size: 18px; color: #333;">
                We sincerely appreciate <strong>{tshirt_supplier_name}</strong> for their timely delivery of high-quality T-shirts.
            </p>
            <p>
                📞 <strong>Contact:</strong> {tshirt_supplier_contact} <br>
                🌐 <a href="{tshirt_supplier_website}" target="_blank" style="font-size: 18px; color: #FFA500;">
                    Visit Root5
                </a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()
