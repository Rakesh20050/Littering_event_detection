import streamlit as st


def render_notifications():

    st.title("🔔 Notifications")

    notifications = [
        {
            "title": "Registration successful",
            "message": "Your identity registration is active.",
            "time": "10:20 AM"
        },
        {
            "title": "Identity verification",
            "message": "Your face embedding has been generated.",
            "time": "10:24 AM"
        }
    ]

    for item in notifications:

        with st.container(border=True):

            st.subheader(item["title"])

            st.write(item["message"])

            st.caption(item["time"])