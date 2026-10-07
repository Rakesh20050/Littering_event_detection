import streamlit as st

from registration import render_registration
from profile import render_profile
from my_reports import render_my_reports
from notifications import render_notifications


st.set_page_config(
    page_title="Smart Monitoring AI - Person",
    page_icon="👤",
    layout="wide"
)


def main():

    st.sidebar.title("👤 Smart Monitoring AI")

    page = st.sidebar.radio(
        "Menu",
        [
            "Registration",
            "My Profile",
            "My Reports",
            "Notifications"
        ]
    )

    if page == "Registration":
        render_registration()

    elif page == "My Profile":
        render_profile()

    elif page == "My Reports":
        render_my_reports()

    elif page == "Notifications":
        render_notifications()


if __name__ == "__main__":
    main()