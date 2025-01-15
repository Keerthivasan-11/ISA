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
            animation: scroll 120s linear infinite; /* Slow and continuous rolling animation */
        }
        .carousel img {
            width: 30%; /* Adjust image size to fit 3 images in one row */
            margin-right: 10px; /* Reduce the margin between images */
            max-height: 600px; /* Ensure images don't exceed max height */
            object-fit: contain;
        }
        /* Keyframes for seamless scroll */
        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-300%); } /* Scroll by 3 images */
        }

        .carousel-four img {
            width: 25%; /* Adjust image size to fit 4 images in one row */
            margin-right: 10px; /* Reduce margin between images */
            max-height: 600px; /* Ensure images don't exceed max height */
            object-fit: contain;
        }

        @keyframes scroll-four {
            0% { transform: translateX(0); }
            100% { transform: translateX(-400%); } /* Scroll by 4 images */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to display laboratory section with rolling effect
def display_lab(lab_name, images, is_three_images=False):
    st.markdown(f"### {lab_name}")
    animation_class = "carousel-four" if not is_three_images else "carousel"
    animation = "scroll-four" if not is_three_images else "scroll"
    st.markdown(
        f"""
        <div class="carousel-container">
            <div class="carousel {animation_class}">
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
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/machines3.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/machines4.jpg",
        ]
    )

    # PG DCF Laboratory (4 images)
    display_lab(
        "PG DCF Laboratory",
        [
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf2.jpg",
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf3.jpg",
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf1.jpg",
           "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf4.jpg",
        ]
    )

    # Process Control Laboratory (3 images)
    display_lab(
        "Process Control Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/process1.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/process2.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/process3.jpg",
        ],
        is_three_images=True
    )

    # UG DCF Laboratory (4 images)
    display_lab(
        "UG DCF Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf1.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf2.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf3.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf4.jpg",
        ]
    )

# Run the app
if __name__ == "__main__":
    app()
