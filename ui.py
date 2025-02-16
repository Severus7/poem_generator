import poem_gen as pg
import streamlit as st

st.title("Poem Generator")

topic = st.text_input("Poem Topic")
choice = st.selectbox("Select the type of poem", ["acrostic", "ballad", "elegy", "epic", "free verse"])

if st.button("Generate Poem"):
    st.markdown(pg.poem_generator(topic, choice))
