import streamlit as st
import pandas as pd
from pymongo import MongoClient

def app():
    try:
        # Check if user is logged in
        if st.session_state["user"] is None:
            st.warning("Please login")
            return
        
        # Check if year is provided
        if not st.session_state["year"]:
            st.warning("Please enter year")
            return
        
        client = MongoClient('mongodb+srv://spcece2025:spc_ec123@cluster0.ibqe72a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # Assuming MongoDB is running locally
        db = client[st.session_state['user'] + '_placement']
        collection = db[st.session_state['year']]

        def display_table(data):
            st.table(data)
        
        st.title("Placement") 
        st.write("----------------------------------------------------------------")    
        # Selection Box for Action
        action = st.selectbox('Select Action', ['Add Record', 'Update Record', 'Delete Record'])
        st.write("")
        st.write("-------------------------------------------------------------------")
            

    
        if action == 'Add Record':
            rollno = st.text_input('Enter Roll No:')
            name = st.text_input('Enter Name:')
            mobileno = st.text_input('Enter Mobile No:')
            company_name = st.text_input('Enter Company Name:')
            status = st.selectbox('Enter Status:',['Placed','Unplaced','Internship_Phase'])
            
            if st.button("Add Record"):
                if not rollno:
                    st.warning('Roll No is required.')
                else:
                    data = {'rollno': rollno,
                            'name': name,
                            'mobileno': mobileno,
                            'company_name': company_name,
                            'Status': status}
                    collection.insert_one(data)
                    st.success('Data inserted successfully!')

        elif action == 'Update Record':
            rollnos = collection.distinct('rollno')
            selected_rollno = st.selectbox('Select Roll No to Update:', rollnos)

            name = st.text_input('Name:', value="")
            mobileno = st.text_input('Mobile No:', value="")
            company_name = st.text_input('Company Name:', value="")
            status = st.selectbox('Enter Status:',['Placed','Unplaced','Internship_Phase'])

            if st.button('Update'):
                update_data = {}
                if name:
                    update_data['name'] = name
                if mobileno:
                    update_data['mobileno'] = mobileno
                if company_name:
                    update_data['company_name'] = company_name
                if status:
                    update_data['status'] = status

                if update_data:
                    collection.update_one({'rollno': selected_rollno}, {'$set': update_data})
                    st.success('Data updated successfully!')
                else:
                    st.warning('No changes detected.')

        elif action == 'Delete Record':
            # Selection Box for deletion method
            delete_method = st.selectbox('Select Deletion Method', ['Delete by Name', 'Delete by Roll No'])

            if delete_method == 'Delete by Name':
                name_to_delete = st.text_input('Enter Name to Delete:')
                if st.button('Delete'):
                    # Check if name exists in the database
                    if collection.find_one({'name': name_to_delete}) is not None:
                        collection.delete_many({'name': name_to_delete})
                        st.success(f'Data with name {name_to_delete} deleted successfully!')
                    else:
                        st.warning(f'No data found with name {name_to_delete}.')
            
            elif delete_method == 'Delete by Roll No':
                rollnos = collection.distinct('rollno')
                rollno_to_delete = st.selectbox("Select Rollno:",rollnos)          

                if st.button('Delete'):
                    collection.delete_many({'rollno': rollno_to_delete})
                    st.success(f'Data with roll no {rollno_to_delete} deleted successfully!')

        # Show Table
        if st.button('Show Table'):
            cursor = collection.find({}, {'_id': 0}).sort('rollno', 1)
            df = pd.DataFrame(list(cursor))
            display_table(df)
    except Exception as e:
        st.warning(f"Something went wrong: {str(e)}")

     