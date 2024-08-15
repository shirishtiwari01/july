import streamlit as st
from PIL import Image
image=Image.open('bank.jpeg')
st.image(image,caption='Welcome to XYZ Bank')
st.title('Loan Calculator')
st.header('XYZ Bank of India')
x=st.number_input('Enter your amount')
y=st.number_input('Enter your salary')
if y>50000:
    st.write('Congratulations')
    st.balloons()
else:
    st.write('Sorry')

st.checkbox('Do you have a credit card')
st.sidebar.header('Schemes from Loan dept. ')
