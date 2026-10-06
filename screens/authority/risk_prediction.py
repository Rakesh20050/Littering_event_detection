import streamlit as st
import pandas as pd


def render_risk_prediction():

    st.header(
        "Future Risk Prediction"
    )

    st.write(
        "The risk model estimates which campus locations "
        "are likely to experience future littering activity."
    )

    st.subheader(
        "Predicted Locations"
    )

    predictions = pd.DataFrame(
        {
            "Location": [
                "Cafeteria",
                "Main Gate",
                "Parking Area",
                "Block A",
                "Library",
            ],
            "Predicted Risk": [
                0.94,
                0.87,
                0.81,
                0.69,
                0.48,
            ],
            "Risk Level": [
                "Very High",
                "High",
                "High",
                "Medium",
                "Low",
            ],
        }
    )

    st.dataframe(
        predictions,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.subheader(
        "Feature Importance"
    )

    features = pd.DataFrame(
        {
            "Feature": [
                "Historical incidents",
                "Time of day",
                "Footfall",
                "Bin availability",
                "Cleaning delay",
                "Weekend activity",
            ],
            "Importance": [
                0.31,
                0.20,
                0.13,
                0.14,
                0.12,
                0.10,
            ],
        }
    )

    st.bar_chart(
        features.set_index(
            "Feature"
        )
    )

    st.divider()

    st.subheader(
        "Prediction Model"
    )

    st.write(
        "**Model:** XGBoost"
    )

    st.write(
        "**Input:** Verified historical incidents + "
        "location/time/context features"
    )

    st.write(
        "**Output:** Future littering risk score"
    )

    st.warning(
        "Risk prediction concerns locations and patterns, "
        "not individual guilt."
    )