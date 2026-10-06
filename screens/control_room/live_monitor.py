"""
CleanWatch AI - Control Room Live Monitor

Displays the live camera stream coming from
the CleanWatch AI server.
"""

import streamlit as st


AI_SERVER_URL = "http://127.0.0.1:8000"


def render_live_monitor():

    st.title("🎥 Control Room — Live Monitor")

    st.caption(
        "Live camera feed received through the CleanWatch AI server"
    )

    col1, col2 = st.columns([3, 1])

    with col1:

        st.subheader("Camera 01")

        # Browser displays the MJPEG stream
        st.markdown(
            f"""
            <img
                src="{AI_SERVER_URL}/camera/video"
                width="100%"
            />
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.subheader("Camera Status")

        st.success("● CAMERA ONLINE")

        st.write("Camera ID")
        st.code("CAMERA_01")

        st.write("Source")
        st.write("Laptop Webcam")

        st.divider()

        st.subheader("AI Pipeline")

        st.write("🟢 Frame Capture")
        st.write("🟡 Object Detection")
        st.write("🟡 Tracking")
        st.write("🟡 Identity")
        st.write("🟡 Event Analysis")

        st.divider()

        st.info(
            "AI detection results will appear here "
            "when the perception pipeline is connected."
        )


if __name__ == "__main__":

    render_live_monitor()