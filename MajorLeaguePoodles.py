from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Major League Poodles", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Using local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

#Load assetts
lottie_coding= load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_Xa1iTX.json")

img_lottie_animation = Image.open("Images/Ace.png")
img_lottie_animation_2 = Image.open("Images/HappyAce.png")
img_lottie_animation_3 = Image.open("Images/Toy.png")
img_lottie_animation_4 = Image.open("Images/Cute.png")
#Header section
with st.container():
    st.subheader("Hello, welcome to the Major League Poodles Website!!!")
    st.title("Our Poodles are fully bred poodles, AKC and Genetically tested")
    st.write("Ace: Is a Red Abstract Male Standard Poodle")
    st.write("Ginger: Is a Red Female standard poodle")
    st.write("[Follow us on Instagram >](https://www.instagram.com/majorleaguepoodles/)")

#What we do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column: 
        st.header("About us")
        st.write("##")
        st.write(
            """
            - We are breeders located in California.
            - All of our poodles are bred, raised, and loved indoors to produce happy, healthy pets for those seeking the best family companion!
            - We are a small, in-home breeding program where we prioritize giving each dog and puppy the best care that we can.
            - We cherish all of our animals and enjoy sharing the love of a Poodle with other individuals and families!
            """
        )
with right_column:
    st_lottie(lottie_coding, height=300, key="poodles")

#Images 
with st.container():
    st.write("---")
    st.header("Images of Ace and Ginger")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)


        with text_column:
            st.subheader("Puppy dog eyes")
            st.write(
                """
                A picture of Ace staring into the abyss
                """
            )


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation_2)


        with text_column:
            st.subheader("Happy Dog")
            st.write(
                """
                A dog is the only thing on earth that loves you more than they love themselves.
                """
            )

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation_3)


        with text_column:
            st.subheader("Guarding my toy")
            st.write(
                """
                Paw patrol on duty, protecting his toy
                """
            )

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation_4)


        with text_column:
            st.subheader("Cutie")
            st.write(
                """
                Love is in the air :heart:
                """
            )

#What we do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column: 
        st.header("How to get a puppy from us")
        st.write("##")
        st.write(
            """
            - Pricing may vary between $2,800- $5,400.
            - You will be able to take your puppy home 10 weeks after birth.
            - If you're interested in a puppy from Major League Poodles, please contact us with the contact form below. You'll be asked to provide information about yourself and what you are looking for so we can help you find the right match. Once you apply, We will get back to you about availability, pricing and next steps.
            """
        )

#-- contact form--
with st.container():
    st.write("---")
    st.header("Contact us")
    st.write("##")

    #Documentation form
    contact_form = """
    <form action="https://formsubmit.co/jennypere17@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Information about yourself and what you are looking for"></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html= True)
with right_column:
    st.empty()
