import streamlit as st

def build_header(hdr: str, title: str, layout='wide',side='auto', p: str=''):
    st.set_page_config(
        page_title= title,
        layout= layout,
        initial_sidebar_state= side
    )
    st.write(hdr)
    st.markdown(p,unsafe_allow_html=True)


def breakrows():
    st.write('''
            <br>
            <br>
            <br>
            <br>
            ''',unsafe_allow_html=True)
    
#filtragem dos dados pelo top definido
def top_categories(data, top: int, label: str):
    top_make_data = data[label].value_counts().nlargest(top).index
    filtered_data = data[data[label].isin(top_make_data)]
    return filtered_data