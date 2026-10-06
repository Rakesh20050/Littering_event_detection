import streamlit as st
from datetime import datetime


def render_report_screen():

    st.header("Report an Environmental Issue")

    st.write(
        "Report litter, overflowing bins, illegal dumping, or other "
        "cleanliness problems."
    )

    with st.form("report_form"):

        location = st.selectbox(
            "Location",
            [
                "Main Gate",
                "Cafeteria",
                "Library",
                "Block A",
                "Block B",
                "Parking Area",
                "Bus Stop",
                "Other",
            ],
        )

        issue_type = st.selectbox(
            "Issue Type",
            [
                "Litter on ground",
                "Overflowing bin",
                "Illegal dumping",
                "Waste accumulation",
                "Other",
            ],
        )

        description = st.text_area(
            "Description",
            placeholder="Describe the issue..."
        )

        image = st.file_uploader(
            "Upload an optional image",
            type=["jpg", "jpeg", "png"],
        )

        submitted = st.form_submit_button(
            "Submit Report",
            use_container_width=True,
        )

    if submitted:

        report_id = (
            "USR-"
            + datetime.now().strftime("%Y%m%d%H%M%S")
        )

        report = {
            "id": report_id,
            "location": location,
            "issue_type": issue_type,
            "description": description,
            "time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "status": "Submitted",
        }

        if "user_reports" not in st.session_state:
            st.session_state.user_reports = []

        st.session_state.user_reports.append(report)

        st.success(
            f"Report {report_id} submitted successfully."
        )

        st.info(
            "The report will be sent to the CleanWatch AI backend "
            "for processing."
        )