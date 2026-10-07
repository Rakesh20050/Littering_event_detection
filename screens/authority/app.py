import streamlit as st

from dashboard import render_dashboard
from notifications import render_notifications
from incident_reports import render_incident_reports
from hotspot_alerts import render_hotspot_alerts


st.set_page_config(
    page_title="Smart Monitoring AI - Authority",
    page_icon="🚨",
    layout="wide"
)


def main():

    st.sidebar.title("🚨 Smart Monitoring AI")

    st.sidebar.caption(
        "Authority Portal"
    )

    page = st.sidebar.radio(
        "Menu",
        [
            "Dashboard",
            "Notifications",
            "Incident Reports",
            "Hotspot Alerts"
        ]
    )

    if page == "Dashboard":
        render_dashboard()

    elif page == "Notifications":
        render_notifications()

    elif page == "Incident Reports":
        render_incident_reports()

    elif page == "Hotspot Alerts":
        render_hotspot_alerts()


if __name__ == "__main__":
    main()