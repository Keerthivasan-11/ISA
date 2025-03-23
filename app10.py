import streamlit as st

def main():
    st.title("Indian Engineers Elite Challenge 2022 - Thanksgiving Video")
    
    st.write("## Watch the Official Thanksgiving Video")
    st.video("https://github.com/Keerthivasan-11/ISA/blob/main/WhatsApp%20Video%202025-03-23%20at%2010.34.44.mp4")
    
    st.write("## Share Your Gratitude")
    st.write("Upload a short Thanksgiving video to express your gratitude and celebrate the success of the challenge.")
    
    # Upload video
    video_file = st.file_uploader("Upload your video (MP4, MOV, AVI)", type=["mp4", "mov", "avi"])
    
    if video_file is not None:
        st.video(video_file)
        st.success("Video uploaded successfully!")

        # Additional input for captions or messages
        message = st.text_area("Add a caption or message for your video:")
        
        if st.button("Post Video"):
            st.write("✅ Your video has been posted with the following message:")
            st.write(message)
            st.write("Thank you for sharing your gratitude!")
    else:
        st.info("Please upload a video to proceed.")

if __name__ == "__main__":
    main()
