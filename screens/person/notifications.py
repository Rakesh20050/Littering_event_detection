import streamlit as st


def render_notifications():

    st.header("Notifications")

    notifications = [
        {
            "title": "Report Received",
            "message": (
                "Your cleanliness report has been "
                "received by the control room."
            ),
            "type": "success",
        },
        {
            "title": "Cleanup Completed",
            "message": (
                "A reported waste location near "
                "the cafeteria has been cleaned."
            ),
            "type": "success",
        },
        {
            "title": "System Update",
            "message": (
                "CleanWatch AI is monitoring the "
                "campus camera network."
            ),
            "type": "info",
        },
    ]

    for notification in notifications:

        with st.container(border=True):

            st.subheader(
                notification["title"]
            )

            st.write(
                notification["message"]
            )

            if notification["type"] == "success":
                st.success("Notification")

            else:
                st.info("Notification")