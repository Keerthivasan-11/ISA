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
            max-width: 100%;
            position: relative;
            overflow: hidden;
        }
        .carousel {
            display: flex;
            animation: scroll 10s linear infinite; /* Continuous rolling animation */
        }
        .carousel img {
            width: 80%; /* Adjust the image size */
            margin-right: 20px; /* Add spacing between images */
            max-height: 500px; /* Limit the image height */
            object-fit: contain;
        }
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
                {''.join([f'<img src="{img}" alt="{lab_name} Image">' for img in images])} <!-- Duplicate images for seamless rolling -->
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

# Run the app
if __name__ == "__main__":
    app()
