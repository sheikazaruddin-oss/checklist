import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Pilot Checklist",
    page_icon="✈️",
    layout="wide"
)

# -------------------------------------------------
# LOGO
# -------------------------------------------------
st.image("logo.png", width=180)

st.title("✈️ Pilot Checklist System")
st.caption("Interactive Pilot Checklist Application")

# -------------------------------------------------
# CHECKLIST DATA
# -------------------------------------------------
checklist = {
    "AFTER START": [
        "Flaps - Up",
        "Ground Tower Freq",
        "Transponder Set",
        "Altimeter Set",
        "FMS Set WPT",
        "Fuel",
    ],

    "CLIMB": [
        "Lights - As Req",
        "Ignition - As Req",
        "Ice Protection - Set",
        "Power - Set",
        "Flaps - As Req",
    ],

    "CRUISE": [
        "Power - Set",
        "Ice Protection - Set",
        "Engine Instr - Norm",
        "Trend Mont - Compl",
    ],

    "DESCENT": [
        "Ice Protection - Set",
        "Pitot/Static Ht - Set",
        "Passenger Adv - Brf",
        "Power - Set",
        "Condition Lvr",
        "Fuel Sel - Both",
        "Lights - On",
        "GPS/NAV Sw - Set",
    ],

    "PRE-LANDING": [
        "Propeller - Max",
        "Flaps - Set",
        "Ignition - As Req",
    ],
}

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "checked_items" not in st.session_state:
    st.session_state.checked_items = {}

for section, items in checklist.items():
    for item in items:
        key = f"{section}_{item}"

        if key not in st.session_state.checked_items:
            st.session_state.checked_items[key] = False

# -------------------------------------------------
# RESET FUNCTION
# -------------------------------------------------
def reset_checklist():
    for key in st.session_state.checked_items:
        st.session_state.checked_items[key] = False

# -------------------------------------------------
# STYLING
# -------------------------------------------------
st.markdown(
    """
    <style>

    .stApp {
        background-color: #0f172a;
    }

    h1, h2, h3, h4, p, label {
        color: white !important;
    }

    .check-card {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 10px;
    }

    .status-green {
        background-color: #16a34a;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        text-align: center;
        font-weight: bold;
    }

    .status-red {
        background-color: #dc2626;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        text-align: center;
        font-weight: bold;
    }

    .section-box {
        background-color: #111827;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 25px;
        border: 1px solid #374151;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# PROGRESS BAR
# -------------------------------------------------
total_items = sum(len(items) for items in checklist.values())
completed_items = sum(st.session_state.checked_items.values())

progress = completed_items / total_items

st.subheader("Checklist Completion Status")

st.progress(progress)

st.write(f"Completed: {completed_items} / {total_items}")

# -------------------------------------------------
# RESET BUTTON
# -------------------------------------------------
if st.button("🔄 Reset Checklist"):
    reset_checklist()
    st.rerun()

st.divider()

# -------------------------------------------------
# CHECKLIST DISPLAY
# -------------------------------------------------
for section, items in checklist.items():

    st.markdown(
        f"""
        <div class="section-box">
        <h2>{section}</h2>
        </div>
        """,
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
                f"""
                <div class="check-card">
                    <h4>{item}</h4>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:

            if checked:
                st.markdown(
                    """
                    <div class="status-green">
                        CHECKED
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:
                st.markdown(
                    """
                    <div class="status-red">
                        PENDING
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.divider()

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.caption("Pilot Checklist Web Application")