import streamlit as st
from streamlit_option_menu import option_menu
import Year,About, Authentication, Internship, Placement, Records, Statistics

#defining sessions
if "year" not in  st.session_state:
    st.session_state['year']=None
if "user" not in  st.session_state:
    st.session_state['user']=None   
key=Authentication.set_user_session()
st.session_state['user']=key

st.set_page_config(
    page_title="SPC ECE RECORD WEB",
    page_icon="📂",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:        

            app = option_menu(
                menu_title='SPC_ECE',
                options=['Year','About', 'Authentication', 'Internship', 'Placement', 'Records', 'Statistics'],
                icons=['calendar-check','house-fill','person-circle','trophy-fill','check-square','info-circle-fill','pie-chart'],
                menu_icon='database-add',
                default_index=1,
               styles={
                      "container": {"padding": "5!important", "background-color": "black"},
                      "icon": {"color": "white", "font-size": "23px"}, 
                      "nav-link": {
                          "color": "white",
                          "font-size": "20px",
                          "text-align": "left",
                          "margin": "0px",
                          "--hover-color": "#413f4d",
                      },
                      "nav-link-selected": {"background-color": "#1a06cc","font-weight": "normal","color":"white"},
                  })

        if app == "Year":
             Year.app()
        elif app=="About":
            About.app()     
        elif app == "Authentication":
            Authentication.app()    
        elif app == "Internship":
            Internship.app()        
        elif app == 'Placement':
            Placement.app()
        elif app == 'Records':
            Records.app()
        elif app == 'Statistics':
            Statistics.app()
    


multi_app = MultiApp()
multi_app.run()
# Checking for user session and displaying login status in sidebar
if key is not None:
    st.sidebar.write(f"Logged in as: {st.session_state['user']}")
    if st.sidebar.button("Sign out"):
        st.session_state['user'] = None
        st.sidebar.success("Logged out successfully")