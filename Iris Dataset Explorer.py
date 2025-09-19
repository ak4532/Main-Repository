import streamlit as st
import pandas as pd
import plotly.express as px

#Set page title and icon
st.set_page_config(page_title="Iris Dataset Explorer", page_icon="🌸")
st.title("Iris Dataset Explorer 🌸")

# Sidebar Navigation
page = st.sidebar.selectbox("Select a Page", ['Home', 'Data Overview', 'Exploratory Data Analysis', 'Extras'])

df = pd.read_csv("iris.csv")

# Home Page
if page == 'Home':
    st.header("Iris Dataset Explorer!")
    st.subheader("Welcome to our Iris Dataset Explorer app!")
    st.write("""
    This app provides an interactive platform to explore the famous Iris dataset.
    You can visualize the distribution of data, explore relationships between features, and even make predictions on new data!
             Use the sidebar to navigate through the sections.
    """)
    st.image('https://bouqs.com/blog/wp-content/uploads/2021/11/iris-flower-meaning-and-symbolism.jpg>', caption="The Iris Flower")


# Data Overview Page
elif page == 'Data Overview':
    st.header("Data Overview")

    st.subheader("About the Data")
    st.write("""
        The Iris dataset is one of the most famous datasets in the literature of machine learning and data analysis.
        It contains 150 samples of iris flowers from three different species: (Iris-setosa, Iris-versicolor, and Iris-virginica).
        For each flower, the datset includes length and width of the sepals and petals.
        """)
    st.image('<https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png>', caption="Iris Dataset")

# Dataset Display
st.subheader("Quick Glance at the Data")    
if st.checkbox("Show DataFrame"):
    st.write(df)

# Shape of Dataset
if st.checkbox("Show Shape of Dataset"):
    st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# Exploratory Data Analysis (EDA)
elif page == 'Exploratory Data Analysis':
    st.title("📊 Exploratory Data Analysis (EDA)")

    st.subheader("Select the type of visualization you'd like to explore:")
    eda_type = st.multiselect("Visualization Options", ['Histograms', 'Box Plots', 'Scatter Plots', 'Count PLots'])

if 'Histograms' in eda_type:
    st.subheader("Histograms - Visualizing Numerical Distributions")
    h_selected_col = st.selectbox(" Slect a numerical column for histogram:", num_cols)
    if h_selected_col:
        chart_title = f"Distribution of {h_selected_col.title().replace('_', ' ')}"
        if st.checkbox("Show by Speicies"):
            st.plotly_chart(px.histogram(df, x=h_selected_col, color="species", title=chart_title,
barmode='overlay'))
        else:
            st.plotly_chart(px.histogram(df, x=h_selected_col, title=chart_title))

if 'Box Plots' in eda_type:
    st.subheader("Box Plots - Visualizing Numerical Distributions")
    b_selected_col = st.selectbox("Select a numerical column for box plot:", num_cols)
    if b_selected_col:
        chart_title = f"Distribution of {b_selected_col.title().replace('_', ' ')}"
        st.plotly_chart(px.box(df, x="species", y=b_selected_col, title =chart_title, color="species"))

if 'Scatter Plots' in eda_type:
    st.subheader("Scatter Plots - Visualizing Relationships")
    selected_col_x = st.selectbox("Select x-axis variable:", num_cols)
    selected_col_y = st.selectbox("Select y-axis variable:", num_cols)
    if selected_col_x and selected_col_y:
        chart_title = f"{selected_col_x.title().replace('_', ' ')} vs{selected_col_y.title().replace('_', ' ')}"
        st.plotly_chart(px.scatter(df, x=selected_col_x, y=selected_col_y, color="species", title=chart_title))

if 'Count Plots' in eda_type:
    st.subheader("Count Plots - Visualizing Categorical Distributions")
    selected_col = st.selectbox("Select a categorical variable:", obj_cols)
    if selected_col:
        chart_title = f"Count of {selected_col.title().replace('_', ' ')}"
        st.plotly_chart(px.histogram(df, x=selected_col, color='species', title=chart_title))

# Extras Page
st.title("Adding Columns")

col1, col2, col3 =st.columns(3)

with col1:
    st.header("A cat")
    st.image("<https://static.streamlit.io/examples/cat.jpg>")

with col2:
    st.header("A dog")
    st.image("<https://static.streamlit.io/examples/dog.jpg>")

with col3:
    st.header("A owl")
    st.image("<https://static.streamlit.io/examples/owl.jpg>")


# Adding Tabs

st.title("Adding Tabs")
tab1, tab2, tab3 = st.tabs(["First Tab", "Second Tab", "Third Tab"])

with tab1:
    st.write("Place whatever you want here! This is your first tab.")

with tab2:
    st.write("This is tab 2!")
    st.image("<https://static.streamlit.io/examples/dog.jpg>")

with tab3:
    st.write("The best for last")

    if st.button("Click me for a surprise!"):
        st.balloons()

# Adding a Container

st.title("Adding a Container")

container = st.container(boarder = True)
container.write("This is inside the container")
st.write("This is outside the container")

# Now insert some more inside the container
container.write("This is also inside too")

# Additinal Features

st.divider()