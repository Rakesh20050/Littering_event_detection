import streamlit as st


def render_cleanup_monitor():

    st.title("🧹 Cleanup Monitoring")

    st.caption(
        "Track cleanup actions following verified incidents"
    )

    tasks = [
        {
            "incident": "INC-001",
            "location": "Cafeteria",
            "status": "Assigned",
            "priority": "High"
        },
        {
            "incident": "INC-002",
            "location": "Block A",
            "status": "In Progress",
            "priority": "Medium"
        },
        {
            "incident": "INC-003",
            "location": "Parking",
            "status": "Completed",
            "priority": "Low"
        }
    ]

    for task in tasks:

        with st.container(border=True):

            col1, col2, col3, col4 = st.columns(4)

            col1.write(
                f"**{task['incident']}**"
            )

            col2.write(
                task["location"]
            )

            col3.write(
                task["status"]
            )

            col4.write(
                task["priority"]
            )