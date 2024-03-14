import streamlit as st

def app():
    st.title("About")
    st.write("-----------------------------------------")
    st.markdown('<h3 style="color: #079beb;">SPC_ECE RECORD WEB</h3>', unsafe_allow_html=True)

    st.write("")
    
    # Introduction
    st.write("The SPC_ECE Record Web is a platform designed by the Student Placement Coordinator (SPC) of the Electronics and Communication Engineering (ECE) department. It serves as a centralized database system to maintain records of different years, aiding the SPC in efficiently managing student placement-related data.")
    
    # Features
    st.markdown('<h3 style="color: #079beb;">Key Features:</h3>', unsafe_allow_html=True)
    st.markdown("- <span style='color: #5fd9ac;'>Internship Records:</span> Keeps track of both summer and winter internships.", unsafe_allow_html=True)
    st.markdown("- <span style='color: #5fd9ac;'>Placement Records:</span> Manages placement details of students.", unsafe_allow_html=True)
    st.markdown("- <span style='color: #5fd9ac;'>Statistics:</span> Provides statistics on placed and unplaced students.", unsafe_allow_html=True)
    st.write("")
    
    # Creator Information
    st.markdown('<h3 style="color: #079beb;">Creators:</h3>', unsafe_allow_html=True)
    st.write("----------------------------------------------")

    col1, col2 = st.columns(2)  # Create two columns
    
    # Creator 1
    with col1:
        st.write("**Creator 1:**")
        st.image("creater1.png", width=200)
        st.write("- **Name:** Neel Sheth")
        st.write("- **Email:** neelsheth708@gmail.com")
        st.write("- [LinkedIn](https://www.linkedin.com/creator1)")
    
    # Creator 2
    with col2:
        st.write("**Creator 2:**")
        st.image("creater1.png", width=200)
        st.write("- **Name:** Creator 2 Name")
        st.write("- **Email:** creator2@example.com")
        st.write("- [LinkedIn](https://www.linkedin.com/creator2)")
    st.write("----------------------------------------------")


