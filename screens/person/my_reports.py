import streamlit as st


def render_my_reports():

    st.header("My Reports")

    reports = st.session_state.get(
        "user_reports",
        []
    )

    if not reports:
        st.info(
            "You have not submitted any reports yet."
        )
        return

    st.metric(
        "Total Reports",
        len(reports)
    )

    st.divider()

    for report in reversed(reports):

        with st.container(border=True):

            col1, col2, col3 = st.columns(
                [2, 3, 2]
            )

            with col1:
                st.write(
                    f"**{report['id']}**"
                )

            with col2:
                st.write(
                    f"{report['issue_type']} "
                    f"— {report['location']}"
                )

            with col3:
                st.write(
                    report["status"]
                )

            st.caption(
                report["time"]
            )

            if report["description"]:
                st.write(
                    report["description"]
                )