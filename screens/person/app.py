import streamlit as st

from screens.person.report_screen import render_report_screen
from screens.person.my_reports import render_my_reports
from screens.person.notifications import render_notifications


st.set_page_config(
    page_title="Smart Monitoring AI - Person",
    page_icon="♻️",
    layout="wide",
)

st.title("♻️ Smart Monitoring AI")
st.caption("Person / Student Application")

st.sidebar.title("Smart Monitoring AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Report an Issue",
        "My Reports",
        "Notifications",
    ],
)

st.sidebar.divider()
st.sidebar.success("AI Server: Online")
st.sidebar.success("Database: Connected")

if page == "Report an Issue":
    render_report_screen()

elif page == "My Reports":
    render_my_reports()

elif page == "Notifications":
    render_notifications()