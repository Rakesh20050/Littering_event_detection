import streamlit as st
import json


def render_reports():

    st.title("📄 Authority Reports")

    st.caption(
        "Generate summaries of incidents, hotspots and AI performance"
    )

    # --------------------------------
    # REPORT TYPE
    # --------------------------------

    report_type = st.selectbox(
        "Report Type",
        [
            "Daily Incident Report",
            "Weekly Authority Report",
            "Hotspot Analysis Report",
            "AI Model Performance Report"
        ]
    )

    # --------------------------------
    # DATE RANGE
    # --------------------------------

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input(
            "Start Date"
        )

    with col2:
        end_date = st.date_input(
            "End Date"
        )

    st.divider()

    # --------------------------------
    # REPORT PREVIEW
    # --------------------------------

    st.subheader("Report Preview")

    st.write(
        f"### {report_type}"
    )

    st.write(
        f"Period: {start_date} → {end_date}"
    )

    report_data = {
        "total_incidents": 86,
        "verified_incidents": 64,
        "rejected_incidents": 8,
        "pending_incidents": 14,
        "high_risk_hotspots": 2,
        "cleanup_completed": 15,
        "ai_model": "CleanWatch-AI-v1.0"
    }

    st.json(report_data)

    st.divider()

    # --------------------------------
    # DOWNLOAD JSON
    # --------------------------------

    report_json = json.dumps(
        report_data,
        indent=4
    )

    st.download_button(
        label="⬇️ Download Report",
        data=report_json,
        file_name="cleanwatch_authority_report.json",
        mime="application/json"
    )

    st.success(
        "Report generated successfully."
    )