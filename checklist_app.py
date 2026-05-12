import streamlit as st
import time

st.set_page_config(
    page_title="Pilot Checklist",
    page_icon="✈️",
    layout="centered"
)

defaults = {
    "Approach": {
        "lights": "OFF",
        "flaps": 0
    },
    "Departure": {
        "lights": "ON",
        "flaps": 10
    },
    "En Route": {
        "lights": "OFF",
        "flaps": 0
    }
}

for page, values in defaults.items():
    if f"{page}_lights" not in st.session_state:
        st.session_state[f"{page}_lights"] = values["lights"]

    if f"{page}_flaps" not in st.session_state:
        st.session_state[f"{page}_flaps"] = values["flaps"]

    if f"{page}_lights_loading" not in st.session_state:
        st.session_state[f"{page}_lights_loading"] = False


def reset_page(page):
    st.session_state[f"{page}_lights"] = defaults[page]["lights"]
    st.session_state[f"{page}_flaps"] = defaults[page]["flaps"]
    st.session_state[f"{page}_lights_loading"] = False


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

    .panel {
        background-color: #1e293b;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #334155;
        margin-bottom: 20px;
    }

    .section-title {
        font-size: 22px;
        font-weight: bold;
        color: white;
        margin-bottom: 14px;
    }

    .light-status-on {
        background-color: #16a34a;
        color: white;
        padding: 12px;
        border-radius: 12px;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
    }

    .light-status-off {
        background-color: #475569;
        color: white;
        padding: 12px;
        border-radius: 12px;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
    }

    .light-status-loading {
        background-color: #f97316;
        color: white;
        padding: 12px;
        border-radius: 12px;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
    }

    .flap-panel {
        width: 230px;
        height: 310px;
        background: linear-gradient(145deg, #111827, #020617);
        border: 3px solid #334155;
        border-radius: 18px;
        position: relative;
        margin: auto;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.55);
    }

    .flap-title {
        position: absolute;
        left: 20px;
        top: 35px;
        color: white;
        font-size: 24px;
        font-weight: 900;
        writing-mode: vertical-rl;
        text-orientation: upright;
        letter-spacing: 2px;
    }

    .flap-slot {
        position: absolute;
        left: 105px;
        top: 45px;
        width: 14px;
        height: 210px;
        background-color: #020617;
        border-radius: 12px;
        border: 2px solid #1e293b;
    }

    .flap-label {
        position: absolute;
        left: 60px;
        color: white;
        font-size: 25px;
        font-weight: bold;
    }

    .flap-zero { top: 38px; }
    .flap-ten { top: 103px; }
    .flap-twenty { top: 168px; }
    .flap-thirty { top: 230px; }

    .flap-handle {
        position: absolute;
        left: 115px;
        width: 95px;
        height: 38px;
        background: linear-gradient(145deg, #f8fafc, #94a3b8);
        border-radius: 8px;
        box-shadow: 0px 5px 10px rgba(0,0,0,0.45);
        transform: skewX(-12deg);
    }

    .flap-pointer {
        position: absolute;
        left: 96px;
        width: 35px;
        height: 8px;
        background-color: #d1d5db;
        border-radius: 6px;
    }

    .flap-warning {
        position: absolute;
        bottom: 18px;
        left: 28px;
        color: white;
        font-size: 13px;
        font-weight: bold;
        text-align: center;
        line-height: 16px;
    }

    div.stButton > button {
        background-color: #2563eb;
        color: white;
        font-size: 15px;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        padding: 9px 18px;
        width: 100%;
    }

    div.stButton > button:hover {
        background-color: #1d4ed8;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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


def light_control(page):
    lights_key = f"{page}_lights"
    loading_key = f"{page}_lights_loading"

    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>TAXI / LANDING LIGHTS</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 2])

    with col1:
        if st.button("ON", key=f"{page}_on"):
            if st.session_state[lights_key] != "ON":
                st.session_state[loading_key] = True
                st.rerun()

    with col2:
        if st.button("OFF", key=f"{page}_off"):
            st.session_state[lights_key] = "OFF"
            st.session_state[loading_key] = False
            st.rerun()

    with col3:
        if st.session_state[loading_key]:
            st.markdown("<div class='light-status-loading'>TURNING ON...</div>", unsafe_allow_html=True)
            time.sleep(2)
            st.session_state[lights_key] = "ON"
            st.session_state[loading_key] = False
            st.rerun()

        elif st.session_state[lights_key] == "ON":
            st.markdown("<div class='light-status-on'>ON</div>", unsafe_allow_html=True)

        else:
            st.markdown("<div class='light-status-off'>OFF</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


def flap_control(page):
    flaps_key = f"{page}_flaps"
    selected = st.session_state[flaps_key]

    positions = {
        0: 48,
        10: 113,
        20: 178,
        30: 240
    }

    handle_top = positions[selected]

    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>FLAPS</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("0°", key=f"{page}_flap_0"):
            st.session_state[flaps_key] = 0
            st.rerun()

        if st.button("10°", key=f"{page}_flap_10"):
            st.session_state[flaps_key] = 10
            st.rerun()

        if st.button("20°", key=f"{page}_flap_20"):
            st.session_state[flaps_key] = 20
            st.rerun()

        if st.button("30°", key=f"{page}_flap_30"):
            st.session_state[flaps_key] = 30
            st.rerun()

    with col2:
        st.markdown(
            f"""
            <div class="flap-panel">
                <div class="flap-title">WING FLAPS</div>

                <div class="flap-label flap-zero">0°</div>
                <div class="flap-label flap-ten">10°</div>
                <div class="flap-label flap-twenty">20°</div>
                <div class="flap-label flap-thirty">30°</div>

                <div class="flap-slot"></div>

                <div class="flap-pointer" style="top:{handle_top + 15}px;"></div>
                <div class="flap-handle" style="top:{handle_top}px;"></div>

                <div class="flap-warning">
                    AVOID SLIPS WITH<br>
                    FLAPS EXTENDED
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)


tab1, tab2, tab3 = st.tabs(["Approach", "Departure", "En Route"])

with tab1:
    page = "Approach"
    light_control(page)
    flap_control(page)

    if st.button("🔄 Reset Approach", key="reset_approach"):
        reset_page(page)
        st.rerun()

with tab2:
    page = "Departure"
    light_control(page)
    flap_control(page)

    if st.button("🔄 Reset Departure", key="reset_departure"):
        reset_page(page)
        st.rerun()

with tab3:
    page = "En Route"
    light_control(page)
    flap_control(page)

    if st.button("🔄 Reset En Route", key="reset_enroute"):
        reset_page(page)
        st.rerun()