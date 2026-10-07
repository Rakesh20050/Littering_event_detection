import streamlit as st


def render_activity_log():

    st.title("📋 Activity Log")

    st.caption(
        "History of AI detections, decisions, reviews and actions"
    )

    activity_type = st.sidebar.selectbox(
        "Activity Type",
        [
            "All",
            "AI Detection",
            "Littering Event",
            "Human Review",
            "Identity Match",
            "Cleanup Action",
            "System"
        ]
    )

    activities = [

        {
            "time": "19:32:41",
            "camera": "Camera 01",
            "activity": "AI Detection",
            "description": "Person detected",
            "track": "Track #17",
            "confidence": "97%"
        },

        {
            "time": "19:32:44",
            "camera": "Camera 01",
            "activity": "Identity Match",
            "description": "Registered person matched",
            "track": "Track #17",
            "confidence": "96%"
        },

        {
            "time": "19:32:51",
            "camera": "Camera 01",
            "activity": "AI Detection",
            "description": "Plastic bottle detected",
            "track": "Track #17",
            "confidence": "91%"
        },

        {
            "time": "19:33:02",
            "camera": "Camera 01",
            "activity": "Littering Event",
            "description": "Hold → Release → Land → Leave",
            "track": "Track #17",
            "confidence": "94%"
        },

        {
            "time": "19:33:04",
            "camera": "Camera 01",
            "activity": "Human Review",
            "description": "Incident sent for verification",
            "track": "Track #17",
            "confidence": "94%"
        },

        {
            "time": "19:34:10",
            "camera": "Camera 02",
            "activity": "Cleanup Action",
            "description": "Cleanup task created",
            "track": "—",
            "confidence": "—"
        }
    ]

    if activity_type != "All":

        activities = [
            item
            for item in activities
            if item["activity"] == activity_type
        ]

    st.subheader(
        f"Recent Activity — {len(activities)} events"
    )

    for item in activities:

        with st.container(border=True):

            col1, col2, col3, col4 = st.columns(4)

            col1.write(
                f"**{item['time']}**"
            )

            col2.write(
                item["activity"]
            )

            col3.write(
                item["description"]
            )

            col4.write(
                item["confidence"]
            )

    st.divider()

    st.subheader("AI Pipeline")

    pipeline = [
        "Camera frame received",
        "Person detection",
        "Waste detection",
        "Object tracking",
        "Identity matching",
        "Person–waste interaction analysis",
        "Temporal event reconstruction",
        "Littering confidence calculation",
        "Human review",
        "Cleanup / escalation"
    ]

    for number, step in enumerate(
        pipeline,
        start=1
    ):

        st.write(
            f"**{number}.** {step}"
        )