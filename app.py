from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Jiya's GATE DA Tracker",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own header/footer/padding so only your tracker shows,
# and make the tracker fill the whole browser window.
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden; height: 0;}
      .block-container, [data-testid="stMainBlockContainer"] {
          padding: 0 !important; max-width: 100% !important;
      }
      iframe {height: 100vh !important; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Your whole website lives in index.html. Edit that file, not this one.
html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
