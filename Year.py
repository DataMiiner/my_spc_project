import streamlit as st

def app():
    st.title("Year Selector")

    st.header("Select a Year Range:")
    year_ranges = [f"{year}-{year + 4}" for year in range(2001, 2101)]
    selected_year_range = st.selectbox("Year Range", year_ranges, format_func=lambda x: f'{x}')
    st.write("---------------------------------------------")
    if st.button('done'):
        st.session_state['year']=selected_year_range
        st.success(f"You selected: {st.session_state['year']}")
        

