import streamlit as st
from pathlib import Path
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parents[2]

REGISTERED_PEOPLE_DIR = (
    PROJECT_ROOT / "data" / "registered_people"
)


def render_registration():

    st.title("👤 Person Registration")

    st.caption(
        "Register your identity for CleanWatch AI recognition."
    )

    st.info(
        "Face registration is used only for authorized identity "
        "matching in the CleanWatch AI system."
    )

    st.divider()

    # ---------------------------------------------------------
    # PERSONAL INFORMATION
    # ---------------------------------------------------------

    st.subheader("1. Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        person_id = st.text_input(
            "Person ID",
            placeholder="CW-00123"
        )

        name = st.text_input(
            "Full Name",
            placeholder="Enter your name"
        )

        college_id = st.text_input(
            "College / Employee ID",
            placeholder="23CS1045"
        )

    with col2:

        department = st.text_input(
            "Department",
            placeholder="Computer Science"
        )

        category = st.selectbox(
            "Category",
            [
                "Student",
                "Faculty",
                "Staff",
                "Security",
                "Other"
            ]
        )

        phone = st.text_input(
            "Contact Number",
            placeholder="Optional"
        )

    st.divider()

    # ---------------------------------------------------------
    # FACE REGISTRATION
    # ---------------------------------------------------------

    st.subheader("2. Face Registration")

    st.write(
        "Capture several face images from different angles "
        "to improve identity matching."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        face_front = st.camera_input(
            "Front Face"
        )

    with col2:
        face_left = st.camera_input(
            "Slight Left"
        )

    with col3:
        face_right = st.camera_input(
            "Slight Right"
        )

    captured = [
        face_front,
        face_left,
        face_right
    ]

    image_count = sum(
        image is not None
        for image in captured
    )

    st.metric(
        "Face Images Captured",
        f"{image_count} / 3"
    )

    st.divider()

    # ---------------------------------------------------------
    # REGISTRATION
    # ---------------------------------------------------------

    if st.button(
        "🔐 Register Person",
        type="primary",
        use_container_width=True
    ):

        if not person_id:
            st.error("Please enter a Person ID.")
            return

        if not name:
            st.error("Please enter your name.")
            return

        if image_count < 3:
            st.warning(
                "Please capture all three face images."
            )
            return

        person_folder = (
            REGISTERED_PEOPLE_DIR / person_id
        )

        person_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        # Save registration information
        profile_file = (
            person_folder / "profile.txt"
        )

        profile_file.write_text(
            f"Person ID: {person_id}\n"
            f"Name: {name}\n"
            f"College/Employee ID: {college_id}\n"
            f"Department: {department}\n"
            f"Category: {category}\n"
            f"Phone: {phone}\n"
            f"Registered At: "
            f"{datetime.now().isoformat()}\n"
        )

        # Save face images
        image_names = [
            "front.jpg",
            "left.jpg",
            "right.jpg"
        ]

        for image, filename in zip(
            captured,
            image_names
        ):

            image_bytes = image.getvalue()

            (
                person_folder / filename
            ).write_bytes(image_bytes)

        st.success(
            "Person registration completed successfully."
        )

        st.info(
            "Next step: the identity AI will generate "
            "face embeddings from the registered images."
        )

        st.write(
            "**Identity status:** Registration complete"
        )

        st.write(
            "**Embedding status:** Pending AI processing"
        )