import streamlit as st


def render_incident_reports():

    st.title("🚨 Verified Incident Reports")

    reports = [
        {
            "id": "INC-001",
            "person": "Rahul Kumar",
            "location": "Block A",
            "event": "Plastic bottle littering",
            "confidence": "94%",
            "status": "Verified"
        },
        {
            "id": "INC-002",
            "person": "Unknown",
            "location": "Cafeteria",
            "event": "Paper littering",
            "confidence": "88%",
            "status": "Verified"
        }
    ]

    for report in reports:

        with st.container(border=True):

            st.subheader(
                f"{report['id']} — {report['event']}"
            )

            st.write(
                f"**Person:** {report['person']}"
            )

            st.write(
                f"**Location:** {report['location']}"
            )

            st.write(
                f"**AI confidence:** {report['confidence']}"
            )

            st.success(
                f"Status: {report['status']}"
            )