import streamlit as st


def evidence_box(title):

    st.markdown(
        f"""
        <div style="
            height:220px;
            background:#151515;
            border:1px solid #555;
            border-radius:10px;
            display:flex;
            align-items:center;
            justify-content:center;
            color:#ddd;
            text-align:center;
        ">
            <div>
                <div style="font-size:40px;">
                    🎞️
                </div>
                <b>{title}</b>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_evidence_viewer():

    st.header(
        "Evidence Viewer"
    )

    incident_id = st.selectbox(
        "Incident",
        [
            "INC-1042",
            "INC-1041",
            "INC-1040",
        ],
    )

    st.write(
        f"Evidence package for **{incident_id}**"
    )

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        evidence_box(
            "Before Interaction"
        )

    with c2:
        evidence_box(
            "Release Event"
        )

    with c3:
        evidence_box(
            "After / Waste on Ground"
        )

    st.divider()

    st.subheader(
        "Evidence Metadata"
    )

    metadata = {
        "Camera": "CAM-01",
        "Track ID": "#17",
        "Detection Confidence": "96%",
        "Tracking Confidence": "92%",
        "Identity Confidence": "94%",
        "Event Confidence": "94%",
        "Timestamp": "10:42:18",
    }

    for key, value in metadata.items():

        col1, col2 = st.columns(2)

        col1.write(
            f"**{key}**"
        )

        col2.write(
            value
        )

    st.divider()

    st.subheader(
        "AI Explanation"
    )

    st.info(
        """
        The AI reconstructed a possible littering sequence
        from multiple frames. A person was tracked while
        interacting with a detected waste object. The object
        was subsequently detected on the ground while the
        tracked person moved away.

        Final attribution requires human verification.
        """
    )