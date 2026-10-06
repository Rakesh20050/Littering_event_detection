import streamlit as st
from datetime import datetime


def render_live_monitor():

    st.header("Live AI Monitor")

    # -------------------------------------------------
    # SYSTEM METRICS
    # -------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Active Cameras",
        "8"
    )

    c2.metric(
        "People Tracked",
        "23"
    )

    c3.metric(
        "AI Events Today",
        "17"
    )

    c4.metric(
        "Pending Review",
        "4"
    )

    st.divider()

    # -------------------------------------------------
    # CAMERA + AI DECISION
    # -------------------------------------------------

    left, right = st.columns(
        [2, 1]
    )

    with left:

        st.subheader(
            "Live Camera Feed"
        )

        st.markdown(
            """
            <div style="
                height:350px;
                background:#111;
                border:2px dashed #555;
                border-radius:12px;
                display:flex;
                align-items:center;
                justify-content:center;
                color:#ddd;
                text-align:center;
            ">
                <div>
                    <div style="font-size:50px;">📹</div>
                    <div style="font-size:22px;">
                        CAM-01
                    </div>
                    <div>
                        Main Gate Camera
                    </div>
                    <div style="margin-top:10px;">
                        Live CCTV stream will appear here
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.subheader(
            "Current AI Detections"
        )

        a, b, c, d = st.columns(4)

        a.metric(
            "Person",
            "1"
        )

        b.metric(
            "Waste",
            "1"
        )

        c.metric(
            "Bin",
            "0"
        )

        d.metric(
            "Track ID",
            "#17"
        )

    with right:

        st.subheader(
            "AI Event Analysis"
        )

        st.warning(
            "Possible littering detected"
        )

        st.write(
            "**Temporal reconstruction**"
        )

        st.progress(
            0.94,
            text=(
                "Hold → Release → "
                "Land → Leave"
            ),
        )

        st.write(
            "**Identity recognition**"
        )

        st.info(
            "Track #17 → Registered Person 023"
        )

        st.caption(
            "Identity recognition and event attribution "
            "are separate AI decisions."
        )

        st.write(
            "**Evidence confidence**"
        )

        st.progress(
            0.94,
            text="94%"
        )

        st.write(
            "**Current status**"
        )

        st.warning(
            "Waiting for human verification"
        )

    st.divider()

    # -------------------------------------------------
    # AI PIPELINE
    # -------------------------------------------------

    st.subheader(
        "AI Pipeline State"
    )

    pipeline = [
        ("Person Detection", "Completed"),
        ("Waste Detection", "Completed"),
        ("Tracking", "Completed"),
        ("Identity Matching", "Completed"),
        ("Interaction Analysis", "Completed"),
        ("Temporal Reconstruction", "Completed"),
        ("Context Analysis", "Completed"),
        ("Evidence Scoring", "Completed"),
        ("Human Review", "Pending"),
    ]

    for name, status in pipeline:

        col1, col2 = st.columns(
            [4, 1]
        )

        col1.write(name)

        if status == "Completed":
            col2.success(status)

        else:
            col2.warning(status)

    st.caption(
        f"Last update: "
        f"{datetime.now().strftime('%H:%M:%S')}"
    )