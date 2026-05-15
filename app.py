import streamlit as st

from utils.ui import (
    inject_dark_theme,
    render_gameplay,
    render_hero,
    render_sidebar,
    render_theme_selection,
)

st.set_page_config(
    page_title="AI Escape Room",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_dark_theme()

if "game_phase" not in st.session_state:
    st.session_state.game_phase = "theme_select"

render_sidebar()
render_hero()

if st.session_state.game_phase == "theme_select":
    render_theme_selection()
elif st.session_state.game_phase in ("playing", "complete"):
    render_gameplay()
