import streamlit as st

st.set_page_config(
    page_title="Pilot Checklist",
    page_icon="✈️",
    layout="centered"
)

checklist = {
    "CLIMB": [
        "Lights – As Req",
        "Ignition – As Req",
        "Ice Protection - Set",
        "Power - Set",
        "Flaps – As Req",
    ],
    "ATC Interaction": [
        "Approach: Ask for weather",
        "Departure: Confirm next waypoint",
        "En Route: Confirm altitude/heading",
    ],
}

if "checked_items" not in st.session_state:
    st.session_state.checked_items = {}

for section, items in checklist.items():
    for item in items:
        key = f"{section}_{item}"
        if key not in st.session_state.checked_items:
            st.session_state.checked_items[key] = False

def reset_checklist():
    for key in st.session_state.checked_items:
        st.session_state.checked_items[key] = False

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f172a;
    }

    h1, h2, h3, h4, p, label {
        color: white !important;
    }

    .logo-center {
        display: flex;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .logo-center img {
        width: 180px;
        border-radius: 16px;
        mix-blend-mode: screen;
    }

    .title-center {
        text-align: center;
        font-size: 44px;
        font-weight: 800;
        color: white;
        margin-bottom: 35px;
    }

    .section-title {
        background-color: #1e293b;
        color: white;
        padding: 16px;
        border-radius: 12px;
        font-size: 26px;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 18px;
        border: 1px solid #334155;
    }

    .item-box {
        background-color: #1e293b;
        padding: 16px;
        border-radius: 12px;
        border: 1px solid #334155;
        font-size: 21px;
        font-weight: 600;
        color: white;
        margin-bottom: 12px;
    }

    .status-green {
        background-color: #16a34a;
        color: white;
        padding: 12px 18px;
        border-radius: 20px;
        text-align: center;
        font-weight: bold;
        font-size: 16px;
        margin-top: 6px;
    }

    .status-red {
        background-color: #dc2626;
        color: white;
        padding: 12px 18px;
        border-radius: 20px;
        text-align: center;
        font-weight: bold;
        font-size: 16px;
        margin-top: 6px;
    }

    div[data-testid="stCheckbox"] {
        transform: scale(1.7);
        margin-top: 15px;
        margin-left: 12px;
    }

    div.stButton > button {
        background-color: #2563eb;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        padding: 12px 22px;
    }

    div.stButton > button:hover {
        background-color: #1d4ed8;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="logo-center">
        <img src="logo.png">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title-center">
        ✈️ Pilot Checklist System
    </div>
    """,
    unsafe_allow_html=True
)

total_items = sum(len(items) for items in checklist.values())
completed_items = sum(st.session_state.checked_items.values())
progress = completed_items / total_items

st.subheader("Checklist Completion Status")
st.progress(progress)
st.write(f"Completed: {completed_items} / {total_items}")

if st.button("🔄 Reset Checklist"):
    reset_checklist()
    st.rerun()

st.divider()

for section, items in checklist.items():

    st.markdown(
        f"<div class='section-title'>{section}</div>",
        unsafe_allow_html=True
    )

    for item in items:
        key = f"{section}_{item}"

        col1, col2, col3 = st.columns([1, 5, 2])

        with col1:
            checked = st.checkbox(
                "",
                value=st.session_state.checked_items[key],
                key=key
            )

        st.session_state.checked_items[key] = checked

        with col2:
            st.markdown(
                f"<div class='item-box'>{item}</div>",
                unsafe_allow_html=True
            )

        with col3:
            if checked:
                st.markdown(
                    "<div class='status-green'>CHECKED</div>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    "<div class='status-red'>PENDING</div>",
                    unsafe_allow_html=True
                )

    st.divider()