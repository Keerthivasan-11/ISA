import streamlit as st

def app():
    # App Title
    st.title("ISA International Society of Automation Officer List 🌍🤖")

    # Officer List Data
    officers = [
        {"Position": "President 👑", "Name": "Mr. Gopinath PS"},
        {"Position": "President-elect 🤝", "Name": "Mr. Chandran"},
        {"Position": "Treasurer 💰", "Name": "Mr. Saravanan. B"},
        {"Position": "Secretary 📋", "Name": "Mr. Prabhakaran"},
        {"Position": "Program Chair 🎤", "Name": "Mr. Jayaharan C J"},
        {"Position": "Past President 🔙", "Name": "Mrs. Jamuna Saiganesh"},
        {
            "Position": "HoD, Department of Instrumentation Engineering, MIT Campus, Anna University Chennai 🏫",
            "Name": "Dr. Srinivasan",
        },
    ]

    # Display the officer list with emojis
    st.header("✨ Officer List ✨")
    for officer in officers:
        st.subheader(officer["Position"])
        st.write(f"👤 {officer['Name']}")

# If running this app individually
if __name__ == "__main__":
    app()
