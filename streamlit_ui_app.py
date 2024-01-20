import streamlit as st

def llmrag_response(question):
    response_text = 'Response for the question : ' + question
    return response_text

# Declare a form and call methods directly on the returned object
form = st.form(key='my_form')
text_entered = form.text_input(label='Enter the question here ...')
submit_button = form.form_submit_button(label='Submit')

st.write('Press submit to have your name printed below')
if submit_button:
    #st.write(f'Text entered is : {text_entered}')
    resp = llmrag_response(text_entered)
    st.write(f'{resp}')