import streamlit as st

def app():
    st.title("Welcome to ISA MIT Student Chapter!")
    st.subheader("India Engineers Elite Challenge 2025")
    
    st.markdown(
        """
        ### About the Challenge:
        The **India Engineers Elite Challenge 2025** is a state-level competition organized by **ISA South India** and the **Department of Instrumentation Engineering, MIT**. It involves:
        - **Sensor Dynamics**
        - **Process Modeling**
        - **Controller Tuning**
        - **PLC-based Automation**
        - **Embedded System Design**
        
        #### Prize Amounts:
        - 🥇 **1st Prize**: ₹15,000  
        - 🥈 **2nd Prize**: ₹10,000  
        - 🥉 **3rd Prize**: ₹5000  
        
        #### Registration Fees:
        - **ISA Student Members**: ₹1,500  
        - **Without Membership**: ₹2,000  
        
        **Maximum Team Size**: 3 members per team.
        """
    )
    
    st.markdown(
        """
        ### Schedule:
        **March 21th:**
        - **08:30 AM to 09:00 AM**: Registration  
        - **09:00 AM to 10:00 AM**: Inauguration  
        - **10:30 AM to 11:30 AM**: Lab Visit  
        - **11:30 AM to 01:00 PM**: Challenge 1  
        - **01:00 PM to 02:00 PM**: Lunch  
        - **02:00 PM to 04:00 PM**: Challenge 2  
        - **04:30 PM to 06:30 PM**: Challenge 3  
        - **07:30 PM to 08:30 PM**: Dinner  

        **March 22th:**
        - **09:00 AM to 12:30 PM**: Challenge 4  
        - **12:30 PM to 01:30 PM**: Lunch  
        - **01:30 PM to 03:30 PM**: Challenge 5  
        - **04:00 PM to 05:00 PM**: Prize Distribution  
        """
    )
    
    st.markdown(
        """
        ### Facilities Provided:
        - Access to well-equipped labs  
        - Hostel accommodation  
        - Snacks, beverages, breakfast, lunch, and dinner  
        - Internet facilities  
        - Certificate for participation  
        """
    )

    st.markdown(
        """
        ### Event Location:
        **Department of Instrumentation Engineering, MIT**  
        Radha Nagar, Chromepet, Chennai - 600044  
       
        """
    )
    
    st.markdown(
        """
        ### Prerequisites:
        Participants should have knowledge of:
        - Sensors and process dynamics  
        - Differential equations and control theory  
        - Various types of controllers  
        - PLCs and ladder logic programming  
        - Integration of sensors, controllers, and automation systems  
        """
    )

    st.markdown(
        """
        ### Contact Information:
        **Event Organizer**:  
        Mr. G.KEERTHIVASAN, Final Year EIE, President, ISA Student Chapter-MIT  
        **Mobile**: +91 9344810244  
        **Email**: keerthivasangopal2004@gmail.com
        
        """
    )

    # Use the raw URL of the video file from GitHub
    video_url = "https://raw.githubusercontent.com/Keerthivasan-11/ISA/c9674e22e269a36468addc58f58640b2ad4c27a2/isa_4%20(1).mp4"
    
    # Embed the video with increased width and height for portrait orientation
    st.markdown(
       f"""
       <video width="360" height="640" controls>
           <source src="{video_url}" type="video/mp4">
           Your browser does not support the video tag.
       </video>
       """,
       unsafe_allow_html=True
   )

    # Instagram, Gmail, and LinkedIn logos with clickable links
    st.markdown("""
        ### Follow Us on Social Media!
        Check out our latest updates and connect with us:
        <a href="https://www.instagram.com/isa_mit_ei/?igsh=bHluMzM4dngzenJx#" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/1200px-Instagram_logo_2022.svg.png" width="30" height="30" style="display:block;" />
        </a>
        <a href="mailto:mitindiaisastudentchapter@gmail.com" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Gmail_Icon.png/1024px-Gmail_Icon.png" width="30" height="30" style="display:block;" />
        </a>
        <a href="https://www.linkedin.com/in/mitindia-isa-studentchapter-277794348" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="30" height="30" style="display:block;" />
        </a>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    app()
