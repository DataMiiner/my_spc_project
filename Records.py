import streamlit as st
import pandas as pd
from pymongo import MongoClient
def app():
  try:
            client = MongoClient('mongodb+srv://spcece2025:spc_ec123@cluster0.ibqe72a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
  except:
            st.warning("Network Issue")
  def display_table(data):
     st.table(data)
     
  st.title("Records")
  
  st.write("------------------------------------------------")
  
  records=st.selectbox("Select Records:",["Summer Internship","Winter Internship","Placement","Placed","Unplaced"])
  st.write("---------------------------------------------------")
  st.subheader(records)
  try:
          if records=="Summer Internship":
                db = client[st.session_state['user'] + '_internship']
                collection = db[st.session_state['year']]
                cursor = collection.find({'internship_type':'Summer'}, {'_id': 0}).sort([('rollno', 1)])
                df = pd.DataFrame(list(cursor))
                display_table(df)
                 # Download CSV button
                csv_data = df.reset_index().to_csv(index=False)
                st.download_button(
                    label="Download Summer Internship Record",
                    data=csv_data,
                    file_name=f"summer_internship_{st.session_state['year']}.csv",
                    mime="text/csv"
                )
          elif records=="Winter Internship":
                db = client[st.session_state['user'] + '_internship']
                collection = db[st.session_state['year']]
                cursor = collection.find({'internship_type':'Winter'}, {'_id': 0}).sort([('rollno', 1)])
                df = pd.DataFrame(list(cursor))
                display_table(df)
                # Download CSV button
                csv_data = df.reset_index().to_csv(index=False)
                st.download_button(
                    label="Download Winter Internship Record",
                    data=csv_data,
                    file_name=f"Winter_internship_{st.session_state['year']}.csv",
                    mime="text/csv"
                )
          elif records=="Placement":
                db = client[st.session_state['user'] + '_placement']
                collection = db[st.session_state['year']]
                cursor = collection.find({}, {'_id': 0}).sort('rollno', 1)
                df = pd.DataFrame(list(cursor))
                display_table(df)
                # Download CSV button
                csv_data = df.reset_index().to_csv(index=False)
                st.download_button(
                    label="Download Placement Record",
                    data=csv_data,
                    file_name=f"Placement_{st.session_state['year']}.csv",
                    mime="text/csv"
                )
          elif records=="Placed":
                db = client[st.session_state['user'] + '_placement']
                collection = db[st.session_state['year']]
                cursor = collection.find({'Status': 'Placed'}, {'_id': 0}).sort('rollno', 1)
                df = pd.DataFrame(list(cursor))
                display_table(df)
                # Download CSV button
                csv_data = df.reset_index().to_csv(index=False)
                st.download_button(
                    label="Download Placed Students Record",
                    data=csv_data,
                    file_name=f"Placed_student_{st.session_state['year']}.csv",
                    mime="text/csv"
                )
          elif records=="Unplaced":
                db = client[st.session_state['user'] + '_placement']
                collection = db[st.session_state['year']]
                cursor = collection.find({'Status': 'Unplaced'}, {'_id': 0}).sort('rollno', 1)
                df = pd.DataFrame(list(cursor))
                display_table(df)
                # Download CSV button
                csv_data = df.reset_index().to_csv(index=False)
                st.download_button(
                    label="Download Unplaced Students Records",
                    data=csv_data,
                    file_name=f"Unplaced_{st.session_state['year']}.csv",
                    mime="text/csv"
                )
  except:
    
    st.warning("Something Went Wrong")
