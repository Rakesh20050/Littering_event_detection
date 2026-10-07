import streamlit as st


def render_incident_review():

    st.title("🚨 Incident Review")

    st.caption(
        "AI-generated incidents requiring human verification"
    )

    incidents = [
        {
            "id": "INC-001",
            "camera": "CAMERA_01",
            "person": "Rahul Kumar",
            "event": "Plastic bottle littering",
            "confidence": "94%",
            "status": "Pending Review"
        },
        {
            "id": "INC-002",
            "camera": "CAMERA_02",
            "person": "Unknown",
            "event": "Paper disposal",
            "confidence": "72%",
            "status": "Pending Review"
        }
    ]

    for incident in incidents:

        with st.container(border=True):

            st.subheader(
                f"{incident['id']} — {incident['event']}"
            )

            col1, col2, col3 = st.columns(3)

            col1.write(
                f"**Camera:** {incident['camera']}"
            )

            col2.write(
                f"**Person:** {incident['person']}"
            )

            col3.write(
                f"**AI Confidence:** {incident['confidence']}"
            )

            st.write(
                f"**Status:** {incident['status']}"
            )

            c1, c2, c3 = st.columns(3)

            with c1:
                st.button(
                    "✅ Verify",
                    key=f"verify_{incident['id']}"
                )

            with c2:
                st.button(
                    "❌ Reject",
                    key=f"reject_{incident['id']}"
                )

            with c3:
                st.button(
                    "🔍 View Evidence",
                    key=f"evidence_{incident['id']}"
                )