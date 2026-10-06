import streamlit as st


def render_dashboard():

    st.header(
        "Campus Cleanliness Dashboard"
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Incidents",
        "186",
        "+12"
    )

    c2.metric(
        "Verified Incidents",
        "142",
        "76%"
    )

    c3.metric(
        "Active Hotspots",
        "6",
        "+2"
    )

    c4.metric(
        "AI Confidence",
        "91%",
        "+3%"
    )

    st.divider()

    st.subheader(
        "Incident Trend"
    )

    trend = {
        "Monday": 18,
        "Tuesday": 24,
        "Wednesday": 21,
        "Thursday": 31,
        "Friday": 35,
        "Saturday": 28,
        "Sunday": 29,
    }

    st.bar_chart(
        trend
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader(
            "Top Problem Locations"
        )

        locations = {
            "Cafeteria": 42,
            "Main Gate": 31,
            "Parking": 27,
            "Block A": 22,
            "Library": 16,
        }

        st.bar_chart(
            locations
        )

    with right:

        st.subheader(
            "AI Event Types"
        )

        events = {
            "Littering": 112,
            "Illegal Dumping": 18,
            "Overflowing Bin": 26,
            "Pickup": 17,
            "Proper Disposal": 13,
        }

        st.bar_chart(
            events
        )