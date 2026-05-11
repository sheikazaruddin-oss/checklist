import streamlit as st

st.set_page_config(
    page_title="Pilot Checklist",
    page_icon="✈️",
    layout="centered"
)

checklist = {
    "CLIMB": [
        "Light",
        "Ignition",
        "Ice Protection",
        "Power",
        "Flaps",
    ],
    "ATC Interaction": [
        "Approach: Ask for weather",
        "Departure: Confirm next waypoint",
        "En Route: Confirm altitude/heading",
    ],
}

for section, items in checklist.items():
    for item in items:
        key = f"{section}_{item}"
        if key not in st.session_state:
            st.session_state[key] = False

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f172a;
    }

    h1, h2, h3, h4, p, label {
        color: white !important;
    }

    .title-center {
        text-align: center;
        font-size: 34px;
        font-weight: 800;
        color: white;
        margin-bottom: 20px;
    }

    .section-title {
        background-color: #1e293b;
        color: white;
        padding: 10px;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
        margin-top: 18px;
        margin-bottom: 10px;
        border: 1px solid #334155;
    }

    .item-box {
        background-color: #1e293b;
        padding: 9px 12px;
        border-radius: 10px;
        border: 1px solid #334155;
        font-size: 15px;
        font-weight: 500;
        color: white;
        margin-bottom: 6px;
    }

    .status-green {
        background-color: #16a34a;
        color: white;
        padding: 7px 10px;
        border-radius: 16px;
        text-align: center;
        font-weight: bold;
        font-size: 12px;
        margin-top: 3px;
    }

    .status-red {
        background-color: #dc2626;
        color: white;
        padding: 7px 10px;
        border-radius: 16px;
        text-align: center;
        font-weight: bold;
        font-size: 12px;
        margin-top: 3px;
    }

    div[data-testid="stCheckbox"] {
        transform: scale(1.25);
        margin-top: 6px;
        margin-left: 8px;
    }

    div.stButton > button {
        background-color: #2563eb;
        color: white;
        font-size: 15px;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        padding: 9px 18px;
        margin-top: 20px;
    }

    div.stButton > button:hover {
        background-color: #1d4ed8;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# LOGO MOVED 4 SPACES RIGHT
col1, col2, col3 = st.columns([1.4, 2, 0.6])

with col2:
    st.image("logo.png", width=190)

st.markdown(
    """
    <div class="title-center">
        ✈️ Pilot Checklist System
    </div>
    """,
    unsafe_allow_html=True
)

total_items = sum(len(items) for items in checklist.values())

completed_items = 0
for section, items in checklist.items():
    for item in items:
        key = f"{section}_{item}"
        if st.session_state[key]:
            completed_items += 1

progress = completed_items / total_items

st.subheader("Checklist Completion Status")
st.progress(progress)
st.write(f"Completed: {completed_items} / {total_items}")

st.divider()

for section, items in checklist.items():

    st.markdown(
        f"<div class='section-title'>{section}</div>",
        unsafe_allow_html=True
    )

    for item in items:
        key = f"{section}_{item}"

        col1, col2, col3 = st.columns([0.7, 5, 1.6])

        with col1:
            checked = st.checkbox("", key=key)

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

if st.button("🔄 Reset Checklist"):
    for section, items in checklist.items():
        for item in items:
            key = f"{section}_{item}"
            if key in st.session_state:
                del st.session_state[key]

    st.rerun()
