import streamlit as st


AI_SERVER_URL = "http://127.0.0.1:8000"


def render_live_monitor():

    st.title("🎥 Live Camera Monitoring")

    st.caption(
        "Live video received through the CleanWatch AI server"
    )

    camera = st.selectbox(
        "Select Camera",
        [
            "CAMERA_01",
            "CAMERA_02",
            "CAMERA_03"
        ]
    )

    col1, col2 = st.columns([3, 1])

    with col1:

        st.subheader(camera)

        st.markdown(
            f"""
            <img
                src="{AI_SERVER_URL}/camera/video"
                width="100%"
                style="
                    border-radius:10px;
                    border:1px solid #444;
                "
            />
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.subheader("Camera Status")

        st.success("🟢 ONLINE")

        st.write("Camera ID")
        st.code(camera)

        st.write("Stream")
        st.write("Live")

        st.divider()

        st.subheader("AI Pipeline")

        st.write("🟢 Frame Capture")
        st.write("🟢 Person Detection")
        st.write("🟡 Waste Detection")
        st.write("🟡 Tracking")
        st.write("🟡 Identity")
        st.write("🟡 Event Analysis")