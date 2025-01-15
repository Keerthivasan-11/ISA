import streamlit as st

# CSS for rolling carousel
def load_css():
    st.markdown(
        """
        <style>
        .carousel-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            position: relative;
            overflow: hidden;
        }
        .carousel {
            display: flex;
            animation: scroll 60s linear infinite; /* Slow and continuous rolling animation */
        }
        .carousel img {
            width: 100%; /* Adjust the image size */
            margin-right: 20px; /* No spacing between images */
            max-height: 500px; /* Limit the image height */
            object-fit: contain;
        }
        /* Keyframes for seamless scroll */
        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-100%); }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to display laboratory section with rolling effect
def display_lab(lab_name, images):
    st.markdown(f"### {lab_name}")
    st.markdown(
        f"""
        <div class="carousel-container">
            <div class="carousel">
                {''.join([f'<img src="{img}" alt="{lab_name} Image">' for img in images])}
                {''.join([f'<img src="{img}" alt="{lab_name} Image">' for img in images])} <!-- Duplicate images for seamless looping -->
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Main app function
def app():
    # Load the CSS for the rolling carousel
    load_css()
  
    # Laboratory Facilities
    st.title("Laboratory Facilities 🔬")
    st.write("Explore the state-of-the-art laboratories in the Department of Instrumentation Engineering, MIT Campus.")

    # Automation Laboratory
    display_lab(
        "Automation Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/automation.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/automation2.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/automation3.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/automation4.jpg",
        ]
    )

    # Control System Laboratory
    display_lab(
        "Control System Laboratory",
        [
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/control1.jpg",
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/control2.jpg",
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/control3.jpg",
        ]
    )

    # Embedded Laboratory
    display_lab(
        "Embedded Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/embedded1.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/embedded2.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/embedded3.jpg",
        ]
    )

    # Machines Laboratory
    display_lab(
        "Machines Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/machines1.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/machines2.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/machines3.jpg"
        ]
    )

    # PG DCF Laboratory
    display_lab(
        "PG DCF Laboratory",
        [
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf2.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf3.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf1.jpg",
        ]
    )

    # Process Control Laboratory
    display_lab(
        "Process Control Laboratory",
        [
  "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/process1.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/process2.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/process3.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/process4.jpg",
            
        ]
    )

    # UG DCF Laboratory
    display_lab(
        "UG DCF Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf1.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf2.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf3.jpg",
            
        ]
    )

# Run the app
if __name__ == "__main__":
    app()
