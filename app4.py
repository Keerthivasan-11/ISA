import streamlit as st

# Streamlit page configuration


# CSS for image carousel
def load_css():
    st.markdown(
        """
        <style>
        .carousel {
            display: flex;
            overflow: hidden;
            max-width: 100%;
            position: relative;
        }
        .carousel img {
            width: 100%;
            transition: transform 1s ease-in-out;
        }
        .carousel-container {
            position: relative;
            overflow: hidden;
        }
        @keyframes slide {
            0% { transform: translateX(0); }
            20% { transform: translateX(0); }
            25% { transform: translateX(-100%); }
            45% { transform: translateX(-100%); }
            50% { transform: translateX(-200%); }
            70% { transform: translateX(-200%); }
            75% { transform: translateX(-300%); }
            95% { transform: translateX(-300%); }
            100% { transform: translateX(0); }
        }
        .carousel-track {
            display: flex;
            animation: slide 15s infinite;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to display laboratory section
def display_lab(lab_name, images):
    st.markdown(f"### {lab_name}")
    st.markdown(
        f"""
        <div class="carousel-container">
            <div class="carousel">
                <div class="carousel-track">
                    {''.join([f'<img src="{img}" alt="{lab_name} Image">' for img in images])}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Main app function
def app():
    # Load the CSS for carousel
    load_css()
  
    # Laboratory Facilities
    st.title("Laboratory Facilities🔬")
    st.write("Explore the state-of-the-art laboratories in the Department of Instrumentation Engineering, MIT Campus.")

    # Automation Laboratory
    display_lab(
        "Automation Laboratory",
        [
            "https://github.com/Keerthivasan-11/ISA/blob/main/automation.jpg",
            "https://github.com/Keerthivasan-11/ISA/blob/main/automation2.jpg",
            "https://github.com/Keerthivasan-11/ISA/blob/main/automation3.jpg",
            "https://github.com/Keerthivasan-11/ISA/blob/main/automation4.jpg",
        ]
    )

    # Control System Laboratory
    display_lab(
        "Control System Laboratory",
        [
            "https://via.placeholder.com/800x400?text=Control+Lab+1",
            "https://via.placeholder.com/800x400?text=Control+Lab+2",
            "https://via.placeholder.com/800x400?text=Control+Lab+3",
            "https://via.placeholder.com/800x400?text=Control+Lab+4",
        ]
    )

    # Embedded Laboratory
    display_lab(
        "Embedded Laboratory",
        [
            "https://via.placeholder.com/800x400?text=Embedded+Lab+1",
            "https://via.placeholder.com/800x400?text=Embedded+Lab+2",
            "https://via.placeholder.com/800x400?text=Embedded+Lab+3",
            "https://via.placeholder.com/800x400?text=Embedded+Lab+4",
        ]
    )

    # Machines Laboratory
    display_lab(
        "Machines Laboratory",
        [
            "https://via.placeholder.com/800x400?text=Machines+Lab+1",
            "https://via.placeholder.com/800x400?text=Machines+Lab+2",
            "https://via.placeholder.com/800x400?text=Machines+Lab+3",
            "https://via.placeholder.com/800x400?text=Machines+Lab+4",
        ]
    )

    # PG DCF Laboratory
    display_lab(
        "PG DCF Laboratory",
        [
            "https://via.placeholder.com/800x400?text=PG+DCF+Lab+1",
            "https://via.placeholder.com/800x400?text=PG+DCF+Lab+2",
            "https://via.placeholder.com/800x400?text=PG+DCF+Lab+3",
            "https://via.placeholder.com/800x400?text=PG+DCF+Lab+4",
        ]
    )

    # Process Control Laboratory
    display_lab(
        "Process Control Laboratory",
        [
            "https://via.placeholder.com/800x400?text=Process+Control+Lab+1",
            "https://via.placeholder.com/800x400?text=Process+Control+Lab+2",
            "https://via.placeholder.com/800x400?text=Process+Control+Lab+3",
            "https://via.placeholder.com/800x400?text=Process+Control+Lab+4",
        ]
    )

    # UG DCF Laboratory
    display_lab(
        "UG DCF Laboratory",
        [
            "https://via.placeholder.com/800x400?text=UG+DCF+Lab+1",
            "https://via.placeholder.com/800x400?text=UG+DCF+Lab+2",
            "https://via.placeholder.com/800x400?text=UG+DCF+Lab+3",
            "https://via.placeholder.com/800x400?text=UG+DCF+Lab+4",
        ]
    )
