import streamlit as st


def render_ai_analysis():

    st.title("🧠 AI Analysis")

    st.caption(
        "Current outputs from the CleanWatch AI pipeline"
    )

    st.subheader("AI Components")

    components = [
        ("Person Detection", "ACTIVE", "97%"),
        ("Waste Detection", "ACTIVE", "91%"),
        ("Object Tracking", "ACTIVE", "95%"),
        ("Identity Recognition", "ACTIVE", "96%"),
        ("Interaction Analysis", "ACTIVE", "89%"),
        ("Littering Event Detection", "ACTIVE", "94%"),
        ("Decision Engine", "ACTIVE", "92%")
    ]

    for name, status, confidence in components:

        col1, col2, col3 = st.columns(3)

        col1.write(f"**{name}**")
        col2.write(status)
        col3.write(confidence)

    st.divider()

    st.subheader("Current Event Reconstruction")

    steps = [
        "Person detected",
        "Waste detected",
        "Person interacted with waste",
        "Hold state detected",
        "Release state detected",
        "Waste landed",
        "Person moved away",
        "Littering candidate generated"
    ]

    for index, step in enumerate(
        steps,
        start=1
    ):

        st.write(
            f"**{index}.** {step}"
        )