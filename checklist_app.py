import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(
    page_title="Pilot Checklist",
    page_icon="✈️",
    layout="centered"
)

defaults = {
    "Approach": {"lights": "OFF", "flaps": 0},
    "Departure": {"lights": "ON", "flaps": 10},
    "En Route": {"lights": "OFF", "flaps": 0}
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


st.markdown("""
<style>
.stApp { background-color: #0f172a; }

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
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.4, 2, 0.6])
with col2:
    st.image("logo.png", width=190)

st.markdown("""
<div class="title-center">
    ✈️ Pilot Checklist System
</div>
""", unsafe_allow_html=True)


def light_control(page):
    lights_key = f"{page}_lights"
    loading_key = f"{page}_lights_loading"

    st.subheader("TAXI / LANDING LIGHTS")

    col1, col2, col3 = st.columns([1, 1, 3])

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
            st.warning("TURNING ON...")
            time.sleep(2)
            st.session_state[lights_key] = "ON"
            st.session_state[loading_key] = False
            st.rerun()
        elif st.session_state[lights_key] == "ON":
            st.success("ON")
        else:
            st.info("OFF")


def flap_control(page):
    flaps_key = f"{page}_flaps"
    selected = st.session_state[flaps_key]

    positions = {
        0: 35,
        10: 95,
        20: 155,
        30: 215
    }

    handle_top = positions[selected]

    st.subheader("FLAPS")

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
        components.html(f"""
        <div style="
            width:260px;
            height:330px;
            background:linear-gradient(145deg,#111827,#020617);
            border:4px solid #334155;
            border-radius:18px;
            position:relative;
            margin:auto;
            box-shadow:0 8px 25px rgba(0,0,0,0.7);
            font-family:Arial;
        ">

            <div style="
                position:absolute;
                left:25px;
                top:35px;
                color:white;
                font-size:26px;
                font-weight:900;
                writing-mode:vertical-rl;
                text-orientation:upright;
                letter-spacing:2px;
            ">WING FLAPS</div>

            <div style="position:absolute; left:78px; top:25px; color:white; font-size:30px; font-weight:bold;">0°</div>
            <div style="position:absolute; left:78px; top:85px; color:white; font-size:30px; font-weight:bold;">10°</div>
            <div style="position:absolute; left:78px; top:145px; color:white; font-size:30px; font-weight:bold;">20°</div>
            <div style="position:absolute; left:78px; top:205px; color:white; font-size:30px; font-weight:bold;">30°</div>

            <div style="
                position:absolute;
                left:140px;
                top:35px;
                width:16px;
                height:220px;
                background:#020617;
                border-radius:12px;
                border:2px solid #1e293b;
            "></div>

            <div style="
                position:absolute;
                left:125px;
                top:{handle_top + 15}px;
                width:40px;
                height:8px;
                background:#d1d5db;
                border-radius:6px;
            "></div>

            <div style="
                position:absolute;
                left:155px;
                top:{handle_top}px;
                width:95px;
                height:42px;
                background:linear-gradient(145deg,#f8fafc,#94a3b8);
                border-radius:8px;
                box-shadow:0 5px 10px rgba(0,0,0,0.5);
                transform:skewX(-12deg);
            "></div>

            <div style="
                position:absolute;
                bottom:18px;
                left:55px;
                color:white;
                font-size:14px;
                font-weight:bold;
                text-align:center;
                line-height:17px;
            ">
                AVOID SLIPS WITH<br>
                FLAPS EXTENDED
            </div>

        </div>
        """, height=360)


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