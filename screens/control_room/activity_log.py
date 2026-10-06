import streamlit as st
import pandas as pd


def render_activity_log():
    st.title("📋 Control Room Activity Log")
    st.caption("History of AI detections, incident decisions, reviews, and system actions")

    # -----------------------------
    # Filters
    # -----------------------------
    st.sidebar.subheader("Activity Filters")

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

    camera_filter = st.sidebar.selectbox(
        "Camera",
        ["All Cameras", "Camera 01", "Camera 02", "Camera 03"]
    )

    # -----------------------------
    # Mock activity data
    # -----------------------------
    activities = [
        {
            "Time": "19:32:41",
            "Camera": "Camera 01",
            "Activity": "AI Detection",
            "Description": "Person detected",
            "Track ID": "Track #17",
            "Confidence": "97%"
        },
        {
            "Time": "19:32:44",
            "Camera": "Camera 01",
            "Activity": "Identity Match",
            "Description": "Registered person matched",
            "Track ID": "Track #17",
            "Confidence": "96%"
        },
        {
            "Time": "19:32:51",
            "Camera": "Camera 01",
            "Activity": "AI Detection",
            "Description": "Plastic bottle detected",
            "Track ID": "Track #17",
            "Confidence": "91%"
        },
        {
            "Time": "19:33:02",
            "Camera": "Camera 01",
            "Activity": "Littering Event",
            "Description": "Hold → Release → Land → Leave",
            "Track ID": "Track #17",
            "Confidence": "94%"
        },
        {
            "Time": "19:33:04",
            "Camera": "Camera 01",
            "Activity": "Human Review",
            "Description": "Incident sent for verification",
            "Track ID": "Track #17",
            "Confidence": "94%"
        },
        {
            "Time": "19:33:25",
            "Camera": "Camera 02",
            "Activity": "AI Detection",
            "Description": "Person detected",
            "Track ID": "Track #21",
            "Confidence": "95%"
        },
        {
            "Time": "19:34:10",
            "Camera": "Camera 02",
            "Activity": "Cleanup Action",
            "Description": "Cleanup task created",
            "Track ID": "—",
            "Confidence": "—"
        },
        {
            "Time": "19:35:18",
            "Camera": "Camera 03",
            "Activity": "System",
            "Description": "Camera connection verified",
            "Track ID": "—",
            "Confidence": "—"
        }
    ]

    df = pd.DataFrame(activities)

    # -----------------------------
    # Apply filters
    # -----------------------------
    if activity_type != "All":
        df = df[df["Activity"] == activity_type]

    if camera_filter != "All Cameras":
        df = df[df["Camera"] == camera_filter]

    # -----------------------------
    # Summary metrics
    # -----------------------------
    st.subheader("Activity Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Activities",
        len(df)
    )

    col2.metric(
        "AI Detections",
        len(df[df["Activity"] == "AI Detection"])
    )

    col3.metric(
        "Littering Events",
        len(df[df["Activity"] == "Littering Event"])
    )

    col4.metric(
        "Human Reviews",
        len(df[df["Activity"] == "Human Review"])
    )

    st.divider()

    # -----------------------------
    # Activity table
    # -----------------------------
    st.subheader("Recent Activity")

    if len(df) == 0:
        st.info("No activities match the selected filters.")
    else:
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    # -----------------------------
    # Selected activity
    # -----------------------------
    st.divider()

    st.subheader("Activity Details")

    if len(df) > 0:

        selected_index = st.selectbox(
            "Select an activity",
            range(len(df)),
            format_func=lambda i:
                f"{df.iloc[i]['Time']} — "
                f"{df.iloc[i]['Activity']} — "
                f"{df.iloc[i]['Description']}"
        )

        selected = df.iloc[selected_index]

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Time:**", selected["Time"])
            st.write("**Camera:**", selected["Camera"])
            st.write("**Activity:**", selected["Activity"])

        with col2:
            st.write("**Track ID:**", selected["Track ID"])
            st.write("**Confidence:**", selected["Confidence"])
            st.write("**Description:**", selected["Description"])

    # -----------------------------
    # AI pipeline explanation
    # -----------------------------
    st.divider()

    st.subheader("AI Pipeline Activity")

    st.write(
        """
        The activity log represents the sequence of decisions produced by
        the CleanWatch AI pipeline.
        """
    )

    pipeline_steps = [
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

    for step_number, step in enumerate(pipeline_steps, start=1):
        st.write(f"**{step_number}.** {step}")