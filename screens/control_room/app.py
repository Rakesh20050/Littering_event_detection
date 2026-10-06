import streamlit as st

from screens.control_room.live_monitor import (
    render_live_monitor
)

from screens.control_room.incident_review import (
    render_incident_review
)

from screens.control_room.evidence_viewer import (
    render_evidence_viewer
)

from screens.control_room.activity_log import (
    render_activity_log
)


st.set_page_config(
    page_title="Smart Monitoring AI - Control Room",
    page_icon="🎥",
    layout="wide",
)

st.title("♻️ Smart Monitoring AI")
st.caption(
    "Control Room — AI Monitoring & Human Verification"
)

st.sidebar.title("Control Room")

page = st.sidebar.radio(
    "Navigation",
    [
        "Live Monitor",
        "Incident Review",
        "Evidence Viewer",
        "Activity Log",
    ],
)

st.sidebar.divider()

st.sidebar.success(
    "AI Server: Online"
)

st.sidebar.success(
    "Database: Connected"
)

st.sidebar.success(
    "Camera Network: Online"
)

if page == "Live Monitor":
    render_live_monitor()

elif page == "Incident Review":
    render_incident_review()

elif page == "Evidence Viewer":
    render_evidence_viewer()

elif page == "Activity Log":
    render_activity_log()