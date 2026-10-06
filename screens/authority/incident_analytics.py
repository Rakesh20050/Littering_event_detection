import streamlit as st
import pandas as pd


def render_incident_analytics():

    st.header(
        "Incident Analytics"
    )

    period = st.selectbox(
        "Analysis Period",
        [
            "Today",
            "Last 7 Days",
            "Last 30 Days",
            "Semester",
        ],
    )

    st.write(
        f"Showing analytics for: **{period}**"
    )

    st.divider()

    data = pd.DataFrame(
        {
            "Category": [
                "Littering",
                "Illegal Dumping",
                "Overflowing Bin",
                "Pickup",
                "Proper Disposal",
            ],
            "Count": [
                112,
                18,
                26,
                17,
                13,
            ],
        }
    )

    st.subheader(
        "Incident Categories"
    )

    st.bar_chart(
        data.set_index("Category")
    )

    st.divider()

    st.subheader(
        "AI vs Human Review"
    )

    review_data = pd.DataFrame(
        {
            "Result": [
                "AI Correct",
                "False Positive",
                "False Negative",
                "Needs More Evidence",
            ],
            "Count": [
                127,
                11,
                4,
                16,
            ],
        }
    )

    st.bar_chart(
        review_data.set_index("Result")
    )

    st.info(
        "Human review results can later be fed into "
        "the model feedback and retraining pipeline."
    )