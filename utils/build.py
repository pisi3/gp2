import streamlit as st

def build_header(hdr: str, title: str, layout='wide',side='auto', p: str=''):
    st.set_page_config(
        page_title= title,
        layout= layout,
        initial_sidebar_state= side
    )
    st.write(hdr)
    st.markdown(p,unsafe_allow_html=True)
