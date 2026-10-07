import streamlit as st


def render_notifications():

    st.title("🔔 Authority Notifications")

    st.caption(
        "Important verified events requiring authority attention"
    )

    alerts = [
        {
            "title": "Verified Littering Incident",
            "person": "Rahul Kumar",
            "location": "Block A Cafeteria",
            "confidence": "94%"
        },
        {
            "title": "New Hotspot Predicted",
            "person": "—",
            "location": "Block B Pathway",
            "confidence": "78%"
        }
    ]

    for alert in alerts:

        with st.container(border=True):

            st.subheader(
                alert["title"]
            )

            st.write(
                f"**Person:** {alert['person']}"
            )

            st.write(
                f"**Location:** {alert['location']}"
            )

            st.write(
                f"**Confidence:** {alert['confidence']}"
            )