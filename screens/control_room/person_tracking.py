import streamlit as st


def render_person_tracking():

    st.title("👤 Person & Identity Tracking")

    st.caption(
        "Live identities associated with tracked people"
    )

    people = [
        {
            "track": "Track #17",
            "name": "Rahul Kumar",
            "id": "CW-00123",
            "confidence": "96%",
            "status": "Active"
        },
        {
            "track": "Track #21",
            "name": "Priya Sharma",
            "id": "CW-00124",
            "confidence": "93%",
            "status": "Active"
        },
        {
            "track": "Track #29",
            "name": "Unknown",
            "id": "—",
            "confidence": "—",
            "status": "Unknown"
        }
    ]

    for person in people:

        with st.container(border=True):

            col1, col2, col3, col4, col5 = st.columns(5)

            col1.write(
                f"**{person['track']}**"
            )

            col2.write(
                person["name"]
            )

            col3.write(
                person["id"]
            )

            col4.write(
                person["confidence"]
            )

            col5.write(
                person["status"]
            )