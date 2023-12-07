import streamlit as st
import difflib

# Set up the title and form for input
st.title('Diff Tool')
text1 = st.text_area("Text 1", height=250)
text2 = st.text_area("Text 2", height=250)

# When the button is pressed, compute the diff
if st.button('Compare'):
    diff = difflib.ndiff(text1.splitlines(keepends=True), text2.splitlines(keepends=True))
    diff_text = ''.join(diff)
    st.text_area("Diff", value=diff_text, height=250, key='diff_output')
