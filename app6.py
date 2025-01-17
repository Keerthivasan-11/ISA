import streamlit as st

# Main function to display the app
def app():
    # Title of the app
    st.title("Meet the Team Behind the Initiative 🚀")

    # About the website maker
    st.header("Website Maker")
    st.write("""
    **Keerthivasan.G**  
    Final Year B.E. student, Electronics and Instrumentation Department.  
    - Played a key role in developing and designing this website.  
    - Demonstrated exceptional technical skills to create a user-friendly interface.  
    """)

    # About the video editor
    st.header("Video Editor")
    st.write("""
    **Shane**  
    Final Year B.E. student, Electronics and Instrumentation Department.  
    - Showcased creative talent by producing high-quality videos.  
    - Captured the essence of the project through excellent video editing skills.  
    """)

    # Closing remarks
    st.markdown("---")
    st.write("Creativity and teamwork in their respective contributions to this initiative.")

# Run the app
if __name__ == "__main__":
    app()
