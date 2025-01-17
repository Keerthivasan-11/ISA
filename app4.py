import streamlit as st

# CSS for rolling carousel and lightbox effect
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
            animation: scroll 120s linear infinite; /* Slow and continuous rolling animation */
        }
        .carousel img {
            width: 80%; /* Further increase image width to make it larger */
            margin-right: 20px; /* Increase margin between images */
            max-height: 1000px; /* Further increase max height for even larger images */
            object-fit: contain;
            cursor: pointer;
        }
        /* Keyframes for seamless scroll */
        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-300%); } /* Scroll by 3 images */
        }

        .carousel-four img {
            width: 70%; /* Increase image width for 4-image layout */
            margin-right: 20px; /* Increase margin between images */
            max-height: 1000px; /* Increase max height for larger images */
            object-fit: contain;
            cursor: pointer;
        }

        @keyframes scroll-four {
            0% { transform: translateX(0); }
            100% { transform: translateX(-400%); } /* Scroll by 4 images */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to display laboratory section with rolling effect and clickable images
def display_lab(lab_name, images, is_three_images=False):
    st.markdown(f"### {lab_name}")
    animation_class = "carousel-four" if not is_three_images else "carousel"
    animation = "scroll-four" if not is_three_images else "scroll"
    st.markdown(
        f"""
        <div class="carousel-container">
            <div class="carousel {animation_class}">
                {''.join([f'<a href="{img}" target="_blank"><img src="{img}" alt="{lab_name} Image"></a>' for img in images])}
                {''.join([f'<a href="{img}" target="_blank"><img src="{img}" alt="{lab_name} Image"></a>' for img in images])} <!-- Duplicate images for seamless looping -->
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

    # Automation Laboratory (4 images)
    display_lab(
        "Automation Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/automation.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/automation2.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/automation3.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/automation4.jpg",
        ]
    )

    # Control System Laboratory (3 images)
    display_lab(
        "Control System Laboratory",
        [
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/control1.jpg",
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/control2.jpg",
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/control3.jpg",
        ],
        is_three_images=True
    )

    # Embedded Laboratory (3 images)
    display_lab(
        "Embedded Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/embedded1.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/embedded2.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/embedded3.jpg",
        ],
        is_three_images=True
    )

    # Machines Laboratory (4 images)
    display_lab(
        "Machines Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/machines1.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/machines2.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/machines3.jpg"
        ]
    )

    # PG DCF Laboratory (4 images)
    display_lab(
        "PG DCF Laboratory",
        [
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf2.jpg",
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf3.jpg",
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf1.jpg"
        ]
    )

    # Process Control Laboratory (3 images)
    display_lab(
        "Process Control Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/process1.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/process2.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/process3.jpg"
        ],
        is_three_images=True
    )

    # UG DCF Laboratory (4 images)
    display_lab(
        "UG DCF Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf1.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf2.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf3.jpg"
        ]
    )

# Run the app
if __name__ == "__main__":
    app()
