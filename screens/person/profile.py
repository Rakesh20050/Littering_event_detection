import streamlit as st


def render_profile():

    st.title("👤 My Profile")

    st.caption(
        "Registered identity information"
    )

    st.subheader("Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Person ID:** CW-00123")
        st.write("**Name:** Rahul Kumar")
        st.write("**College ID:** 23CS1045")

    with col2:

        st.write("**Department:** Computer Science")
        st.write("**Category:** Student")
        st.write("**Registration:** Active")

    st.divider()

    st.subheader("Identity AI Status")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Face Images",
        "3"
    )

    col2.metric(
        "Embedding",
        "Ready"
    )

    col3.metric(
        "Identity Status",
        "Active"
    )

    st.info(
        "Your registered identity can be matched against "
        "authorized CleanWatch AI camera feeds."
    )