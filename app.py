import streamlit as st
import difflib
from st_annotated_text import annotated_text

def process_diff(diff):
    processed_diff = []
    for line in diff:
        if line.startswith('+'):
            # Additions in green
            processed_diff.append((line, "", "#e6ffe6"))
        elif line.startswith('-'):
            # Deletions in red
            processed_diff.append((line, "", "#ffe6e6"))
        else:
            # Unchanged lines
            processed_diff.append(line)
    return processed_diff

# Set up the title and form for input
st.title('Diff Tool')
text1 = st.text_area("Text 1", height=250)
text2 = st.text_area("Text 2", height=250)

# When the button is pressed, compute and display the diff
if st.button('Compare'):
    diff = difflib.ndiff(text1.splitlines(keepends=True), text2.splitlines(keepends=True))
    processed_diff = process_diff(diff)
    annotated_text(*processed_diff)
