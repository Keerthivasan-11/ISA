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
            width: 45%; /* Adjust image size to fit 3 images in one row */
            margin-right: 10px; /* Adjust margin between images */
            max-height: 600px; /* Ensure images don't exceed max height */
            object-fit: contain;
        }
        /* Keyframes for seamless scroll */
        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-300%); } /* Scroll by 3 images */
        }

        .carousel-four img {
            width: 40%; /* Adjust image size to fit 4 images in one row */
            margin-right: 10px; /* Adjust margin between images */
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
                {''.join([f'<img src="{img}" onerror="this.src=\'https://via.placeholder.com/300\'" alt="{lab_name} Image">' for img in images])}
                {''.join([f'<img src="{img}" onerror="this.src=\'https://via.placeholder.com/300\'" alt="{lab_name} Image">' for img in images])} <!-- Duplicate images for seamless looping -->
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

    # FLOW Laboratory (4 images)
    display_lab(
        "FLOW Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/FLOW%201.png",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/FLOW%202.png",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/FLOW%203.png"
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

    # Industrial Instrumentation (3 images)
    display_lab(
        "Industrial Instrumentation",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/II%201.png",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/II%202.png",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/II%201.png"
        ],
        is_three_images=True
    )

    # Transducer Laboratory (4 images)
    display_lab(
        "Transducer Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/TRANSDUCER%201.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/TRANSDUCER%202.jpg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/TRANSDUCER%203.jpg"
        ]
    )

    # Smart Instrumentation Laboratory (Fixed URLs)
    display_lab(
        "Smart Instrumentation Laboratory",
        [
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/smart%20flow%201.jpeg",
            "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/smart%20flow%202.jpeg"
        ]
    )

# Run the app
if __name__ == "__main__":
    app()
