import streamlit as st

def app():
    # App Title
    st.title("ISA International Society of Automation Officer List 🌍🤖")

    # Officer List Data with Corrected Image URLs
    officers = [
        {"Position": "President 👑", "Name": "Mr. Gopinath PS", "Image": "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/Gopinath.jpg"},
        {"Position": "President-elect 🤝", "Name": "Mr. Chandran", "Image": "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/Chandran.jpg"},
        {"Position": "Treasurer 💰", "Name": "Mr. Saravanan. B", "Image": "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/Saravanan_Balakrishnan.png"},
        {"Position": "Secretary 📋", "Name": "Mr. Prabhakaran", "Image": "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/Prabhakaran.jpg"},
        {"Position": "Program Chair 🎤", "Name": "Mr. Jayaharan C J & Mr. Vidurar", "Image": "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/Vidurar.png"},
        {"Position": "Past President 🔙", "Name": "Mrs. Jamuna Saiganesh", "Image": "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/Yamuna.jpg"},
        {
            "Position": "HoD, Department of Instrumentation Engineering, MIT Campus, Anna University Chennai 🏫",
            "Name": "Dr. Srinivasan",
            "Image": "",
        },
        {
            "Position": "Assistant Professor, Student Mentor of ISA MIT Student Chapter 👩‍🏫✨ & Program Chair 🎤",
            "Name": "Dr. M. Mythily",
            "Image": "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/mythili.jpeg",
        },
    ]

    # Display the officer list with images
    st.header("✨ Officer List ✨")
    for officer in officers:
        st.subheader(officer["Position"])
        st.write(f"👤 {officer['Name']}")
        if officer["Image"]:  # Display the image if available
            st.image(officer["Image"], caption=officer["Name"], width=200)

# If running this app individually
if __name__ == "__main__":
    app()
