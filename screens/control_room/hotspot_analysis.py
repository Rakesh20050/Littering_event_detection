import streamlit as st


def render_hotspot_analysis():

    st.title("🗺️ Hotspot Analysis")

    st.caption(
        "Historical hotspot detection and future risk prediction"
    )

    st.subheader("Current Risk Locations")

    hotspots = [
        ("Cafeteria Entrance", 87, "HIGH"),
        ("Block A Pathway", 81, "HIGH"),
        ("Parking Area", 64, "MEDIUM"),
        ("Library Entrance", 29, "LOW")
    ]

    for location, score, risk in hotspots:

        st.write(
            f"**{location}** — {risk} — {score}%"
        )

        st.progress(
            score / 100
        )

    st.divider()

    st.subheader("Next Predicted Hotspot")

    st.success(
        "Block B pathway"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Risk",
        "HIGH"
    )

    col2.metric(
        "Prediction",
        "78%"
    )

    col3.metric(
        "Period",
        "Evening"
    )

    st.divider()

    st.subheader("Hotspot Intelligence")

    st.write(
        "The hotspot model will use historical incident "
        "locations, frequency, time and other available "
        "features to estimate future risk."
    )