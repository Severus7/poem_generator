import poem_gen as pg
import streamlit as st

st.title("Poem Generator")

topic = st.text_input("Poem Topic")

poetry_types = [
    "acrostic", 
    "ballad", 
    "elegy", 
    "epic", 
    "free verse",
    "ghazal",
    "haiku",
    "limerick",
    "ode",
    "sonnet",
    "villanelle"
]

choice = st.selectbox("Select the type of poem", poetry_types)

if st.button("Generate Poem"):
    st.markdown(pg.poem_generator(topic, choice))
