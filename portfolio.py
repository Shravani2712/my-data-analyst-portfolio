import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Shravani Dhuri | Data Analyst Portfolio",
    layout="wide"
)

# Read HTML file
html_file = Path("index.html")
html_content = html_file.read_text(encoding="utf-8")

# Render HTML inside Streamlit
components.html(
    html_content,
    height=3500,
    scrolling=True
)