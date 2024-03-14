import streamlit as st
from pymongo import MongoClient
import random
import string
import smtplib
import re


def set_user_session():
    global user_session
    user_session = st.session_state.get('user')
    return user_session
    
try:    
    # Connect to MongoDB
    client = MongoClient('mongodb+srv://spcece2025:spc_ec123@cluster0.ibqe72a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client['authentication']
    collection = db['id']
except:
  st.warning("Network Warning")
# Function to generate a random password
def generate_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(10))
    return password

# Function to send email with generated password
def send_email(email, password):
  
    sender_email = "spc.ec2025@gmail.com"
    receiver_email = email
    subject = "[SPC_ECE] Your Password was Reset"
    body = f"We wanted to let you know that your SPC_ECE password was reset.---- {password}"
    text=f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    

    # Login to your Gmail account
    server.login(sender_email,"jddq ccsh ujpw hlkf")
    try:
        server.sendmail(sender_email,receiver_email,text)
    except:
       st.warning("OOPs there is error!")
    
    server.quit()
#Function for congrats email
def send_email(email, subject, body):
    sender_email = "spc.ec2025@gmail.com"
    receiver_email = email
    text = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    # Login to your Gmail account
    server.login(sender_email,"jddq ccsh ujpw hlkf")
    try:
        server.sendmail(sender_email,receiver_email,text)
    except:
       st.warning("OOPs there is error!")
    
    server.quit()

# Function to validate email format
def validate_email(email):
    # Regular expression for email validation
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return True
    else:
        return False

# Streamlit app
def app():
    # Initialize session state if it doesn't exist
    if 'user' not in st.session_state:
        st.session_state['user'] = None
    st.header("Authentication")
    st.write("------------------------------------------")
    

    # Selection box for login, signup, or forgot password
    selection = st.selectbox("Select", ["Login", "Sign Up", "Forgot Password"])

    if selection == "Login":
        # Login
        st.subheader("Login")
        login_email = st.text_input("Email")
        login_password = st.text_input("Password", type="password")
        if st.button("Login"):
            user = collection.find_one({"email": login_email, "password": login_password})
            if user:
                st.session_state['user'] = user['username']
                set_user_session()
                st.success("Login Successful")
            else:
                st.error("Invalid Email or Password")
    elif selection == "Sign Up":
          # Sign Up
        st.subheader("Sign Up")
        new_email = st.text_input("Email")
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type="password")
        if st.button("Create Account"):
            # Check if email is in correct format
            if not validate_email(new_email):
                st.error("Please enter a valid email.")
            else:
                # Check if username is unique
                user = collection.find_one({"username": new_username})
                if user:
                    st.error("Username already exists. Please choose a different username.")
                else:
                    # Check if email already exists
                    user = collection.find_one({"email": new_email})
                    if user:
                        st.error("Email already exists. Please use a different email.")
                    else:
                        new_user = {"email": new_email, "username": new_username, "password": new_password}
                        collection.insert_one(new_user)
                        
                        # Send congratulatory email
                        subject = "Welcome  to SPC_ECE_WEB"
                        body = f"Congratulations! You have successfully signed up for SPC EC Web with:\nUsername: {new_username}\nPassword: {new_password}\n\nPlease do not share this information with anyone."

                        send_email(new_email, subject, body)
                        
                        st.success("Account created successfully")
    else:
        # Forgot Password
        st.subheader("Forgot Password")
        forgot_email = st.text_input("Enter your Email to reset password")
        if st.button("Reset Password"):
            user = collection.find_one({"email": forgot_email})
            if user:
                new_password = generate_password()
                collection.update_one({"email": forgot_email}, {"$set": {"password": new_password}})
                send_email(forgot_email, new_password)
                st.success("Password reset email sent. Please check your email for the new password.")
            else:
                st.error("Email not found. Please enter a valid email.")
    
 
            
# Run the app
if __name__ == '__main__':
    app()
