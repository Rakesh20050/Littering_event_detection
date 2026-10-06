import streamlit as st
import pandas as pd


def render_hotspot_analysis():

    st.header(
        "Hotspot Analysis"
    )

    st.write(
        "Historical incidents are spatially clustered to "
        "identify locations with recurring littering activity."
    )

    st.subheader(
        "Detected Hotspots"
    )

    hotspots = pd.DataFrame(
        {
            "Location": [
                "Cafeteria",
                "Main Gate",
                "Parking Area",
                "Block A",
                "Library",
                "Bus Stop",
            ],
            "Incidents": [
                42,
                31,
                27,
                22,
                16,
                14,
            ],
            "Risk Score": [
                0.94,
                0.87,
                0.81,
                0.69,
                0.48,
                0.42,
            ],
            "Cluster": [
                1,
                1,
                2,
                2,
                3,
                3,
            ],
        }
    )

    st.dataframe(
        hotspots,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.subheader(
        "Hotspot Risk Scores"
    )

    st.bar_chart(
        hotspots.set_index(
            "Location"
        )["Risk Score"]
    )

    st.divider()

    st.subheader(
        "Spatial AI Method"
    )

    st.write(
        "**DBSCAN**"
    )

    st.write(
        """
        DBSCAN can group incidents based on spatial
        proximity and identify recurring high-density
        regions without requiring the number of clusters
        to be known beforehand.
        """
    )

    st.info(
        "The final implementation should obtain coordinates "
        "from PostgreSQL/PostGIS."
    )