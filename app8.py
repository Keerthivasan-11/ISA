import streamlit as st

def app():
    # App Title
    st.title("ISA International Society of Automation Officer List 🌍🤖")

    # Officer List Data with Images
    officers = [
        {"Position": "President 👑", "Name": "Mr. Gopinath PS", "Image": "https://github.com/Keerthivasan-11/ISA/blob/main/Gopinath.jpg?raw=true"},
        {"Position": "President-elect 🤝", "Name": "Mr. Chandran", "Image": "https://github.com/Keerthivasan-11/ISA/blob/main/Chandran.jpg?raw=true"},
        {"Position": "Treasurer 💰", "Name": "Mr. Saravanan. B", "Image": "https://github.com/Keerthivasan-11/ISA/blob/main/Saravanan_Balakrishnan.png?raw=true"},
        {"Position": "Secretary 📋", "Name": "Mr. Prabhakaran", "Image": "https://github.com/Keerthivasan-11/ISA/blob/main/Prabhakaran.jpg?raw=true"},
        {"Position": "Program Chair 🎤", "Name": "Mr. Jayaharan C J & Dr. M. Mythily", "Image": "https://github.com/Keerthivasan-11/ISA/blob/main/mythili.jpeg?raw=true"},
        {"Position": "Past President 🔙", "Name": "Mrs. Jamuna Saiganesh", "Image": "https://github.com/Keerthivasan-11/ISA/blob/main/Yamuna.jpg?raw=true"},
        {
            "Position": "HoD, Department of Instrumentation Engineering, MIT Campus, Anna University Chennai 🏫",
            "Name": "Dr. Srinivasan",
            "Image": "",
        },
        {
            "Position": "Assistant Professor, Student Mentor of ISA MIT Student Chapter 👩‍🏫✨",
            "Name": "Dr. M. Mythily",
            "Image": "https://github.com/Keerthivasan-11/ISA/blob/main/mythili.jpeg?raw=true",
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
