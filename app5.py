import streamlit as st

# Load CSS for styling
def load_css():
    st.markdown(
        """
        <style>
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 80%;
            border-radius: 10px;
        }
        .section-title {
            color: #FF5722;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .content {
            text-align: justify;
            margin-bottom: 30px;
            font-size: 18px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Main function
def app():
    # Load CSS styles
    load_css()

    # App title
    st.title("India Elite Challenge 2024 🎉")
    st.markdown(
        """
        The **India Elite Challenge** is an annual flagship event that celebrates innovation, collaboration, and technical excellence.  
        Let's take a moment to relive the incredible memories from the 2024 edition.
        """
    )

    # Section: Inauguration
    st.markdown('<div class="section-title">✨ Inauguration Ceremony</div>', unsafe_allow_html=True)
    st.markdown(
        """
        The event began with a grand inauguration that set the tone for an inspiring and exciting journey. 
        Eminent speakers, faculty members, and participants came together to witness the ceremonial launch.
        """
    )
    st.image(
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/IMG_20240329_092945.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/IMG_20240329_094957.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/20240330_171330.jpg"
        ],
        caption=["Lighting the Lamp of Knowledge", "Eminent Speakers Addressing the Audience", "Participants Welcoming the Challenge"],
        width=600,
    )

    # Section: Last Year's Winners
    st.markdown('<div class="section-title">🏆 Celebrating Last Year’s Champions</div>', unsafe_allow_html=True)
    st.markdown(
        """
        The challenge witnessed outstanding performances from talented teams across the country.  
        Our winners truly embodied the spirit of perseverance, innovation, and technical brilliance.
        """
    )
    st.image(
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/20240330_175816(0).jpg",
        caption="Proud Winners of India Elite Challenge 2024",
        width=600,
        use_column_width="always",
    )

    # Section: Group Photo of Volunteers
    st.markdown('<div class="section-title">💪 The Driving Force: Our Volunteers</div>', unsafe_allow_html=True)
    st.markdown(
        """
        Behind every successful event are the dedicated individuals who work tirelessly to make it happen.  
        Here’s a glimpse of the incredible volunteer team that made the 2024 edition a grand success.
        """
    )
    st.image(
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/20240330_175951.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/20240330_180341.jpg"
        ],
        caption=["Volunteers Celebrating a Successful Event", "The Team Behind the Magic"],
        width=600,
    )

    # Section: Closing Event and Moments
    st.markdown('<div class="section-title">🌟 Memorable Closing Moments</div>', unsafe_allow_html=True)
    st.markdown(
        """
        The India Elite Challenge 2024 concluded with a heartfelt closing ceremony.  
        The shared experiences, camaraderie, and triumphs left an indelible mark on every participant and organizer.
        """
    )
    st.image(
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/IMG_20240330_170641.jpg",
        caption="Cherishing the Closing Ceremony",
        width=600,
        use_column_width="always",
    )

    # Final Note
    st.markdown(
        """
        The India Elite Challenge 2024 was a true celebration of talent and teamwork.  
        We eagerly look forward to the next edition, where new milestones await.  
        **Stay tuned for India Elite Challenge 2025!**
        """
    )

# Run the app
if __name__ == "__main__":
    app()
