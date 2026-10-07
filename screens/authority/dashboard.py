import streamlit as st


def render_dashboard():

    st.title("🚨 Authority Dashboard")

    st.caption(
        "Verified CleanWatch AI notifications"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Verified Incidents",
        "8"
    )

    col2.metric(
        "Open Actions",
        "4"
    )

    col3.metric(
        "Hotspot Alerts",
        "3"
    )

    st.divider()

    st.subheader("Latest Alert")

    st.warning(
        "Verified littering incident detected at Block A."
    )

    st.write(
        "**Person:** Rahul Kumar"
    )

    st.write(
        "**Location:** Block A Cafeteria"
    )

    st.write(
        "**AI confidence:** 94%"
    )

    st.write(
        "**Human verification:** Confirmed"
    )