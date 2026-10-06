import streamlit as st


def render_incident_review():

    st.header("Incident Review")

    incidents = [
        {
            "id": "INC-1042",
            "camera": "CAM-01",
            "track": "#17",
            "identity": "Registered Person 023",
            "event": "Possible Littering",
            "confidence": 0.94,
        },
        {
            "id": "INC-1041",
            "camera": "CAM-03",
            "track": "#08",
            "identity": "Unknown",
            "event": "Possible Littering",
            "confidence": 0.78,
        },
        {
            "id": "INC-1040",
            "camera": "CAM-02",
            "track": "#31",
            "identity": "Registered Person 011",
            "event": "Possible Disposal",
            "confidence": 0.91,
        },
    ]

    st.subheader(
        "Pending AI Incidents"
    )

    selected = st.selectbox(
        "Select Incident",
        incidents,
        format_func=lambda x:
            f"{x['id']} — {x['event']} "
            f"({x['confidence']:.0%})",
    )

    st.divider()

    col1, col2 = st.columns(
        [2, 1]
    )

    with col1:

        st.subheader(
            "Incident Information"
        )

        st.write(
            f"**Incident ID:** "
            f"{selected['id']}"
        )

        st.write(
            f"**Camera:** "
            f"{selected['camera']}"
        )

        st.write(
            f"**Track:** "
            f"{selected['track']}"
        )

        st.write(
            f"**Identity:** "
            f"{selected['identity']}"
        )

        st.write(
            f"**Event:** "
            f"{selected['event']}"
        )

        st.write(
            f"**AI Confidence:** "
            f"{selected['confidence']:.0%}"
        )

    with col2:

        st.subheader(
            "AI Decision"
        )

        st.progress(
            selected["confidence"]
        )

        if selected["confidence"] >= 0.90:
            st.success(
                "High-confidence event"
            )
        elif selected["confidence"] >= 0.75:
            st.warning(
                "Medium-confidence event"
            )
        else:
            st.error(
                "Low-confidence event"
            )

    st.divider()

    st.subheader(
        "Temporal Event Reconstruction"
    )

    events = [
        "Person enters scene",
        "Waste detected",
        "Waste near person's hand",
        "Person releases waste",
        "Waste reaches ground",
        "Person moves away",
    ]

    for i, event in enumerate(events, 1):

        st.write(
            f"**Step {i}:** {event}"
        )

    st.divider()

    st.subheader(
        "Human Verification"
    )

    col1, col2, col3 = st.columns(3)

    if col1.button(
        "✓ Confirm Littering",
        use_container_width=True,
    ):
        st.success(
            f"{selected['id']} verified."
        )

    if col2.button(
        "✕ Reject Event",
        use_container_width=True,
    ):
        st.warning(
            f"{selected['id']} rejected."
        )

    if col3.button(
        "↻ Request More Evidence",
        use_container_width=True,
    ):
        st.info(
            "Incident returned for further evidence."
        )

    feedback = st.text_area(
        "Reviewer Feedback",
        placeholder=(
            "Explain why the AI decision "
            "was correct or incorrect..."
        ),
    )

    if st.button(
        "Save Review Feedback"
    ):
        st.success(
            "Feedback saved for the human-in-the-loop pipeline."
        )