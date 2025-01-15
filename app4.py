import streamlit as st

# Define laboratory image data
labs = {
    "Automation Laboratory": [
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/automation.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/automation2.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/automation3.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/automation4.jpg",
    ],
    "Control System Laboratory": [
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/control1.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/control2.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/control3.jpg",
    ],
    "Embedded Laboratory": [
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/embedded1.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/embedded2.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/embedded3.jpg",
    ],
    "Machines Laboratory": [
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/machines1.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/machines2.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/machines3.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/machines4.jpg",
    ],
    "PG DCF Laboratory": [
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf2.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf3.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf1.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/pgdcf4.jpg",
    ],
    "Process Control Laboratory": [
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/process1.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/process2.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/process3.jpg",
    ],
    "UG DCF Laboratory": [
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf1.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf2.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf3.jpg",
        "https://raw.githubusercontent.com/Keerthivasan-11/ISA/main/ugdcf4.jpg",
    ],
}

# Display lab images as a manual carousel
def display_lab(lab_name, images):
    st.markdown(f"### {lab_name}")

    # Maintain state for the currently displayed image index
    if f"image_index_{lab_name}" not in st.session_state:
        st.session_state[f"image_index_{lab_name}"] = 0

    # Buttons for manual navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("⬅️ Previous", key=f"prev_{lab_name}"):
            st.session_state[f"image_index_{lab_name}"] = (
                st.session_state[f"image_index_{lab_name}"] - 1
            ) % len(images)
    with col2:
        st.image(
            images[st.session_state[f"image_index_{lab_name}"]],
            caption=f"{lab_name} - Image {st.session_state[f'image_index_{lab_name}'] + 1}",
        )
    with col3:
        if st.button("➡️ Next", key=f"next_{lab_name}"):
            st.session_state[f"image_index_{lab_name}"] = (
                st.session_state[f"image_index_{lab_name}"] + 1
            ) % len(images)


# Main app
def app():
    st.title("Laboratory Facilities 🔬")
    st.write(
        "Explore the state-of-the-art laboratories in the Department of Instrumentation Engineering, MIT Campus."
    )

    for lab_name, images in labs.items():
        display_lab(lab_name, images)


# Run the app
if __name__ == "__main__":
    app()
