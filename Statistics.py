import streamlit as st
import pandas as pd
from pymongo import MongoClient
import plotly.express as px

def app():
    try:
        st.title("Placement Statistics")
        st.write("-------------------------------------------------------------------")
        
        # Connect to MongoDB
        client = MongoClient('mongodb+srv://spcece2025:spc_ec123@cluster0.ibqe72a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        db = client[st.session_state['user'] + '_placement']
        collection = db[st.session_state['year']]
        
        st.info("Company's Statistics")
        # Query database to get company-wise placement data
        cursor = collection.find({'company_name': {'$ne': ''}}, {'company_name': 1, '_id': 0})
        df = pd.DataFrame(list(cursor))

        # Count the occurrences of each company
        company_counts = df['company_name'].value_counts().reset_index()
        company_counts.columns = ["Company's Name", "No. of Students"]

        # Display company-wise placement statistics
        st.table(company_counts)
        
        # Download CSV button
        csv_data = company_counts.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name=f"Company_Statistics_{st.session_state['year']}.csv",
            mime="text/csv"
        )

        # Create a pie chart for company-wise placement
        fig = px.pie(company_counts, values='No. of Students', names="Company's Name", title="Company's Statistics")
        st.plotly_chart(fig)
        
        st.info("Placed-Unplaced Statistics")
        
        # Query database to get placed-unplaced data
        cursor1 = collection.find({},{'Status':1,'_id':0})
        df1 = pd.DataFrame(list(cursor1))

        # Count the occurrences of each status (placed or unplaced)
        placement_counts = df1['Status'].value_counts().reset_index()
        placement_counts.columns = ['Status', 'Counts']

        # Display placed-unplaced statistics
        st.table(placement_counts)
        
        # Download CSV button
        csv_data = placement_counts.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name=f"Placement_Statistics_{st.session_state['year']}.csv",
            mime="text/csv"
        )

        # Create a pie chart for placed and unplaced statistics
        fig2 = px.pie(placement_counts, values='Counts', names='Status', title='Placed-Unplaced Statistics')
        st.plotly_chart(fig2)
  
    except Exception as e:
        st.warning("Something Went Wrong")

