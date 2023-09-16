import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()



col1, col2, col3 = st.columns(3)
col2.image(Image.open('profilepic.PNG'))

st.header('Prajeet Singh')

st.info('SDE @Accenture')

icon_size = 20

st_button('youtube', 'https://youtube.com/', 'Insert your youtube link here', icon_size)

st_button('medium', 'https://medium.com/@prajeetkalchuri18', 'Check out my blogs', icon_size)

st_button('linkedin', 'https://www.linkedin.com/in/prajeet-singh-kalchuri/', 'Follow me on LinkedIn', icon_size)


