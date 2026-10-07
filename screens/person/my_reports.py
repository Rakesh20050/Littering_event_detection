import streamlit as st


def render_my_reports():

    st.title("📋 My Reports")

    st.caption(
        "Reports associated with your registered identity"
    )

    reports = [
        {
            "Incident": "INC-00124",
            "Date": "07 Oct 2026",
            "Location": "Block A",
            "Status": "Under Review"
        },
        {
            "Incident": "INC-00098",
            "Date": "02 Oct 2026",
            "Location": "Cafeteria",
            "Status": "Resolved"
        }
    ]

    for report in reports:

        with st.container(border=True):

            col1, col2, col3, col4 = st.columns(4)

            col1.write(
                f"**{report['Incident']}**"
            )

            col2.write(
                report["Date"]
            )

            col3.write(
                report["Location"]
            )

            col4.write(
                report["Status"]
            )