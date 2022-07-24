import streamlit as st


st.write("""
# Subtraction Application
""")

st.header('User Input Parameters')

with st.form(key='my_form'):
    first = st.number_input("First_Number",step=1)
    second = st.number_input("Second_Number",step=1)
    submit= st.form_submit_button(label='Submit')
if submit:
    st.write(first-second)
