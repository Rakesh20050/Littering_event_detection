import streamlit as st

from command_center import render_command_center
from live_monitor import render_live_monitor
from incident_review import render_incident_review
from evidence_viewer import render_evidence_viewer
from person_tracking import render_person_tracking
from ai_analysis import render_ai_analysis
from hotspot_analysis import render_hotspot_analysis
from historical_analytics import render_historical_analytics
from cleanup_monitor import render_cleanup_monitor
from activity_log import render_activity_log
from reports import render_reports


st.set_page_config(
    page_title="Smart Monitoring AI - Control Room",
    page_icon="🖥️",
    layout="wide"
)


def main():

    st.sidebar.title("🖥️ Smart Monitoring AI")

    st.sidebar.caption(
        "AI Control Room"
    )

    page = st.sidebar.radio(
        "Navigation",
        [
            "Command Center",
            "Live Monitoring",
            "Active Incidents",
            "Person & Identity",
            "AI Analysis",
            "Evidence",
            "Human Review",
            "Hotspot Analysis",
            "Historical Analytics",
            "Cleanup Monitoring",
            "Activity Log",
            "Reports"
        ]
    )

    if page == "Command Center":
        render_command_center()

    elif page == "Live Monitoring":
        render_live_monitor()

    elif page == "Active Incidents":
        render_incident_review()

    elif page == "Person & Identity":
        render_person_tracking()

    elif page == "AI Analysis":
        render_ai_analysis()

    elif page == "Evidence":
        render_evidence_viewer()

    elif page == "Human Review":
        render_incident_review()

    elif page == "Hotspot Analysis":
        render_hotspot_analysis()

    elif page == "Historical Analytics":
        render_historical_analytics()

    elif page == "Cleanup Monitoring":
        render_cleanup_monitor()

    elif page == "Activity Log":
        render_activity_log()

    elif page == "Reports":
        render_reports()


if __name__ == "__main__":
    main()