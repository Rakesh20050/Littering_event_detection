import streamlit as st


def render_command_center():

    st.title("🖥️ Smart Monitoring AI — Command Center")

    st.caption(
        "Central AI monitoring, incident intelligence and hotspot analysis"
    )

    # ---------------------------------------------------------
    # SYSTEM STATUS
    # ---------------------------------------------------------

    st.subheader("System Status")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Cameras Online",
        "3 / 3"
    )

    col2.metric(
        "People Detected",
        "247"
    )

    col3.metric(
        "AI Incidents Today",
        "14"
    )

    col4.metric(
        "Pending Review",
        "3"
    )

    st.divider()

    # ---------------------------------------------------------
    # LIVE CAMERA + CURRENT INCIDENT
    # ---------------------------------------------------------

    col1, col2 = st.columns([2.2, 1])

    with col1:

        st.subheader("🎥 Live Camera")

        st.markdown(
            """
            <div style="
                height:320px;
                background:#111;
                border-radius:10px;
                display:flex;
                align-items:center;
                justify-content:center;
                color:white;
                font-size:24px;
            ">
                CAMERA 01 LIVE FEED
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.subheader("🚨 Current AI Event")

        st.warning(
            "Littering candidate detected"
        )

        st.write("**Track:** #17")
        st.write("**Identity:** Rahul Kumar")
        st.write("**Identity confidence:** 96%")
        st.write("**Waste:** Plastic bottle")
        st.write("**Littering confidence:** 94%")

        st.button(
            "Review Incident",
            use_container_width=True
        )

    st.divider()

    # ---------------------------------------------------------
    # QUICK ANALYTICS
    # ---------------------------------------------------------

    st.subheader("📊 Today's AI Activity")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Person Detections", "247")
    col2.metric("Waste Detections", "83")
    col3.metric("Littering Candidates", "14")
    col4.metric("Verified", "8")
    col5.metric("Rejected", "3")

    st.divider()

    # ---------------------------------------------------------
    # TREND
    # ---------------------------------------------------------

    st.subheader("📈 Littering Trend")

    data = {
        "08:00": 1,
        "10:00": 2,
        "12:00": 4,
        "14:00": 3,
        "16:00": 5,
        "18:00": 7,
        "20:00": 4
    }

    max_value = max(data.values())

    for time, value in data.items():

        percentage = (
            value / max_value * 100
        )

        st.markdown(
            f"""
            <div style="margin-bottom:8px;">
                <div style="font-size:13px;">
                    {time} — {value} incidents
                </div>
                <div style="
                    width:100%;
                    background:#eeeeee;
                    height:14px;
                    border-radius:7px;
                ">
                    <div style="
                        width:{percentage}%;
                        height:14px;
                        border-radius:7px;
                        background:#ff4b4b;
                    "></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # ---------------------------------------------------------
    # HOTSPOT SUMMARY
    # ---------------------------------------------------------

    st.subheader("🗺️ Current Hotspot Intelligence")

    hotspots = [
        ("Cafeteria Entrance", "HIGH", 87),
        ("Block A Pathway", "HIGH", 81),
        ("Parking Area", "MEDIUM", 64),
        ("Library Entrance", "LOW", 29)
    ]

    for location, risk, score in hotspots:

        col1, col2, col3 = st.columns([3, 1, 1])

        col1.write(f"**{location}**")
        col2.write(risk)
        col3.write(f"{score}%")

    st.divider()

    st.subheader("🔮 Next Predicted Hotspot")

    st.info(
        "Block B pathway is currently predicted to be the "
        "next high-risk littering location."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Risk",
        "HIGH"
    )

    col2.metric(
        "Prediction Score",
        "78%"
    )

    col3.metric(
        "Expected Period",
        "Evening"
    )