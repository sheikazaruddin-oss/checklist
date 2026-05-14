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

.light-loading-box {
    background-color: #f97316;
    color: white;
    padding: 14px;
    border-radius: 12px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
}

.light-indicator-on {
    width: 95px;
    height: 95px;
    border-radius: 50%;
    background: radial-gradient(circle,#fde68a 0%,#facc15 35%, #ca8a04 75%);
    margin: auto;
    margin-top: 95px;
    box-shadow: 0 0 35px #fde047, 0 0 70px #facc15;
    border: 4px solid #fef3c7;
}

.light-indicator-off {
    width: 95px;
    height: 95px;
    border-radius: 50%;
    background: #334155;
    margin: auto;
    margin-top: 95px;
    border: 4px solid #64748b;
}

.light-label {
    color: white;
    text-align: center;
    font-size: 16px;
    font-weight: bold;
    margin-top: 12px;
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

button, button:hover, button:focus, button:active {
    opacity: 1 !important;
    filter: none !important;
}

iframe {
    opacity: 1 !important;
    filter: none !important;
}

[data-testid="stHorizontalBlock"],
[data-testid="column"],
[data-testid="stMarkdownContainer"] {
    opacity: 1 !important;
    filter: none !important;
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

    col1, col2, col3 = st.columns([1.3, 1.3, 1.6])

    with col1:
        if st.button("Toggle Switch", key=f"{page}_toggle_light"):
            if st.session_state[lights_key] == "ON":
                st.session_state[lights_key] = "OFF"
                st.session_state[loading_key] = False
                st.rerun()
            else:
                st.session_state[loading_key] = True
                st.rerun()

        switch_text = "SWITCH ON" if st.session_state[lights_key] == "ON" else "SWITCH OFF"
        lever_top = 30 if st.session_state[lights_key] == "ON" else 72
        stem_top = 35.5 if st.session_state[lights_key] == "ON" else 80

        components.html(f"""
        <div style="
            width:170px;
            height:170px;
            background:linear-gradient(145deg,#111827,#020617);
            border:4px solid #334155;
            border-radius:18px;
            position:relative;
            font-family:Arial;
        ">
            <div style="
                position:absolute;
                left:36px;
                top:16px;
                width:90px;
                height:90px;
                border-radius:50%;
                border:4px solid #94a3b8;
            "></div>

            <div style="
                position:absolute;
                left:70px;
                top:{stem_top}px;
                width:22px;
                height:7px;
                background:#d1d5db;
                border-radius:6px;
            "></div>

            <div style="
                position:absolute;
                left:86px;
                top:{lever_top}px;
                width:46px;
                height:20px;
                background:linear-gradient(145deg,#f8fafc,#cbd5e1);
                border-radius:10px;
                transform:skewX(-18deg);
                box-shadow:0 4px 10px rgba(0,0,0,0.6);
            "></div>

            <div style="
                position:absolute;
                bottom:12px;
                width:100%;
                text-align:center;
                color:white;
                font-size:16px;
                font-weight:bold;
            ">
                {switch_text}
            </div>
        </div>
        """, height=230)

    with col2:
        if st.session_state[loading_key]:
            st.markdown(
                "<div class='light-loading-box'>TURNING ON...</div>",
                unsafe_allow_html=True
            )

            time.sleep(2)

            st.session_state[lights_key] = "ON"
            st.session_state[loading_key] = False

            st.rerun()

        elif st.session_state[lights_key] == "ON":

            st.markdown("""
<div class="light-indicator-on"></div>
<div class="light-label">LIGHT ON</div>
""", unsafe_allow_html=True)

        else:

            st.markdown("""
<div class="light-indicator-off"></div>
<div class="light-label">LIGHT OFF</div>
""", unsafe_allow_html=True)


def flap_control(page):

    flaps_key = f"{page}_flaps"

    st.subheader("FLAPS")

    selected = st.session_state[flaps_key]

    flap_main_col1, flap_main_col2 = st.columns([2.4, 1])

    with flap_main_col1:

        positions = {
            0: 35,
            10: 95,
            20: 155,
            30: 215
        }

        handle_top = positions[selected]

        components.html(f"""
        <div style="
            width:300px;
            height:340px;
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
                left:22px;
                top:34px;
                color:white;
                font-size:18px;
                font-weight:900;
                writing-mode:vertical-rl;
                text-orientation:upright;
                letter-spacing:1px;
            ">WING FLAPS</div>

            <div style="position:absolute; left:100px; top:25px; color:white; font-size:26px; font-weight:bold;">0°</div>
            <div style="position:absolute; left:100px; top:85px; color:white; font-size:26px; font-weight:bold;">10°</div>
            <div style="position:absolute; left:100px; top:145px; color:white; font-size:26px; font-weight:bold;">20°</div>
            <div style="position:absolute; left:100px; top:205px; color:white; font-size:26px; font-weight:bold;">30°</div>

            <div style="
                position:absolute;
                left:170px;
                top:35px;
                width:16px;
                height:220px;
                background:#020617;
                border-radius:12px;
                border:2px solid #1e293b;
            "></div>

            <div style="
                position:absolute;
                left:153px;
                top:{handle_top + 15}px;
                width:42px;
                height:8px;
                background:#d1d5db;
                border-radius:6px;
            "></div>

            <div style="
                position:absolute;
                left:185px;
                top:{handle_top}px;
                width:90px;
                height:40px;
                background:linear-gradient(145deg,#f8fafc,#94a3b8);
                border-radius:8px;
                box-shadow:0 5px 10px rgba(0,0,0,0.5);
                transform:skewX(-12deg);
            "></div>

            <div style="
                position:absolute;
                bottom:18px;
                left:75px;
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

    with flap_main_col2:

        st.write("")
        st.write("")

        flap_options = [0, 10, 20, 30]

        for flap_value in flap_options:

            if selected == flap_value:

                st.markdown(f"""
                <div style="
                    background-color:#16a34a;
                    color:white;
                    padding:9px 0px;
                    border-radius:10px;
                    text-align:center;
                    font-weight:bold;
                    margin-bottom:12px;
                    width:68px;
                ">
                    {flap_value}°
                </div>
                """, unsafe_allow_html=True)

            else:

                if st.button(f"{flap_value}°", key=f"{page}_flap_{flap_value}"):

                    st.session_state[flaps_key] = flap_value
                    st.rerun()


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
