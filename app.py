import streamlit as st

# Title of the app
st.title("Welcome to My Simple Streamlit App")

# Display text
st.write("This is a basic example of a Streamlit app.")

# Input text
name = st.text_input("Enter your name:")

# Button to display the input
if st.button("Submit"):
    st.write(f"Hello, {name}! Welcome to the app.")

# Sidebar for additional options
st.sidebar.header("Settings")
sidebar_option = st.sidebar.selectbox("Select an option:", ("Option 1", "Option 2", "Option 3"))

st.write(f"You selected {sidebar_option} from the sidebar.")
