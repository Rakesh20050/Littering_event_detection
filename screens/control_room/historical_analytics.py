import streamlit as st


def render_historical_analytics():

    st.title("📊 Historical Analytics")

    st.caption(
        "Historical littering and AI detection analysis"
    )

    # ---------------------------------------------------------
    # SUMMARY
    # ---------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Incidents",
        "186"
    )

    col2.metric(
        "Verified",
        "129"
    )

    col3.metric(
        "Rejected",
        "37"
    )

    col4.metric(
        "Pending",
        "20"
    )

    st.divider()

    # ---------------------------------------------------------
    # WEEKLY TREND
    # ---------------------------------------------------------

    st.subheader("Weekly Incident Trend")

    weekly_data = {
        "Monday": 18,
        "Tuesday": 21,
        "Wednesday": 27,
        "Thursday": 24,
        "Friday": 31,
        "Saturday": 38,
        "Sunday": 27
    }

    maximum = max(
        weekly_data.values()
    )

    for day, count in weekly_data.items():

        percentage = (
            count / maximum * 100
        )

        st.markdown(
            f"""
            <div style="margin:8px 0;">
                <b>{day}</b>
                <span style="float:right;">
                    {count}
                </span>

                <div style="
                    background:#eeeeee;
                    height:12px;
                    border-radius:6px;
                ">
                    <div style="
                        width:{percentage}%;
                        height:12px;
                        background:#ff4b4b;
                        border-radius:6px;
                    "></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # ---------------------------------------------------------
    # LOCATIONS
    # ---------------------------------------------------------

    st.subheader("Incidents by Location")

    locations = [
        ("Cafeteria", 43),
        ("Block A", 38),
        ("Parking", 29),
        ("Block B", 24),
        ("Library", 12)
    ]

    for location, count in locations:

        st.write(
            f"**{location}** — {count} incidents"
        )

    st.divider()

    # ---------------------------------------------------------
    # WASTE TYPES
    # ---------------------------------------------------------

    st.subheader("Waste Type Distribution")

    waste = [
        ("Plastic", 61),
        ("Paper", 42),
        ("Bottle", 37),
        ("Food Waste", 28),
        ("Other", 18)
    ]

    for waste_type, count in waste:

        st.write(
            f"**{waste_type}:** {count}"
        )