import streamlit as st
import difflib


def process_diff(diff):
    processed_diff = []
    for line in diff:
        if line.startswith("+"):
            # Additions in green
            processed_diff.append(f":green[{line}]")
        elif line.startswith("-"):
            # Deletions in red
            processed_diff.append(f":red[{line}]")
        else:
            # Unchanged lines
            processed_diff.append(line)
    return processed_diff


st.set_page_config(
    page_title="Diffchecker",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown("<center><h1>Diffchecker</h1></center>", unsafe_allow_html=True)

cols = st.columns([1, 1])
with cols[0]:
    text1 = st.text_area("Original text", height=250)
with cols[1]:
    text2 = st.text_area("Changed text", height=250)

with st.columns([1, 3, 1])[1]:
    if st.button("Find difference", use_container_width=True):
        diff = difflib.ndiff(text1.splitlines(keepends=True), text2.splitlines(keepends=True))
        processed_diff = process_diff(diff)
        with st.container(border=True):
            st.markdown("<br>".join(processed_diff), unsafe_allow_html=True)
