import streamlit as st

# Sidebar for navigation
page = st.sidebar.selectbox("Select a page", ["Home", "Data Dashboard", "About"])

# Display different pages based on selection
if page =="Home":
    st.title("Welcome to the Home Page")
    st.write("This is the home page of your multi-page app.")

elif page == "Data Dashboard":
    st.title("Data Dashboard")
    st.write("This is where your data visualizations will be go.")

elif page == "About":
    st.title("About")
    st.write("This is an example of a multi-page Streamlit app.")


elif page =="Data Dashboard":
    st.title("Data Dashboard")

    # Example of displaying a DataFrame and chart on the dashboard page
    import pandas as pd
    import plotly.express as px

    # Create sample data
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 23, 45, 15]
    })

    st.write("Here is a sample data data:")
    st.dataframe(data)

    #Create and display a bar chart using Plotly
    fig = px.bar(data, x='Category', y='Values', title='Category Values',
                    labels={'Category': 'Category', 'Values': 'Values'})
    
    #Display the plotly chart in Streamlit
    st.plotly_chart(fig)