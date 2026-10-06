import streamlit as st

from screens.authority.dashboard import render_dashboard
from screens.authority.incident_analytics import (
    render_incident_analytics
)
from screens.authority.hotspot_analysis import (
    render_hotspot_analysis
)
from screens.authority.risk_prediction import (
    render_risk_prediction
)
from screens.authority.reports import (
    render_reports
)


st.set_page_config(
    page_title="Smart Monitoring AI - Authority",
    page_icon="📊",
    layout="wide",
)

st.title("♻️ Smart Monitoring AI")
st.caption(
    "Authority Intelligence & Analytics"
)

st.sidebar.title(
    "Authority Dashboard"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Incident Analytics",
        "Hotspot Analysis",
        "Risk Prediction",
        "Reports",
    ],
)

st.sidebar.divider()

st.sidebar.success(
    "AI Server: Online"
)

st.sidebar.success(
    "Database: Connected"
)

if page == "Dashboard":
    render_dashboard()

elif page == "Incident Analytics":
    render_incident_analytics()

elif page == "Hotspot Analysis":
    render_hotspot_analysis()

elif page == "Risk Prediction":
    render_risk_prediction()

elif page == "Reports":
    render_reports()