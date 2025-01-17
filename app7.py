import streamlit as st

# Main function to display the app
def app():
    # Title of the app
    st.title("Contact Information 📞")

    # Query contact details
    st.header("For Queries Regarding Registration:")
    st.write("""
    **PADMANABAN.G** - 9790702859  
    **NANDHINI M** - 6369145076
    """)

    # Hostel accommodation contact
    st.header("For Queries Regarding Hostel Accommodation:")
    st.write("""
    **KALAISELVAN** - 6369564232
    """)

    # Website-related doubts
    st.header("For Website-Related Doubts:")
    st.write("""
    **Keerthivasan.G** - 9344810244
    """)

    # Closing remarks
    st.markdown("---")
    st.write("Feel free to reach out to the respective contacts for any assistance or doubts.")

# Run the app
if __name__ == "__main__":
    app()
