######## Import the required pacakges ############
import streamlit as st
import google.generativeai as genai
from PIL import Image

####### Provide your api key ###################
api_key="Api_key"
genai.configure(api_key=api_key)

######## Choose the heading ###############
st.header("Image analytics")

########## Upload a file ##################
uploaded_file=st.file_uploader("Upload an image",type=["png","jpg","jpeg"])

if uploaded_file is not None:
    st.image(Image.open(uploaded_file))

############ What you want ask ####################
prompt=st.text_input("Enter the text")

######### Use genai skill ##########################

if st.button("GET RESPONSE"):
    img=Image.open(uploaded_file)
    model=genai.GenerativeModel("gemini-1.0-pro-vision-latest")
    response=model.generate_content([prompt,img])
    st.markdown(response.text)

!streamlit run /content/Streamlit_image_app.py  & npx localtunnel --port 8501 & curl ipv4.icanhazip.com
     
