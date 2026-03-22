import streamlit as st
import random
import time

st.set_page_config(page_title="Automotive CAN Dashboard", layout="wide")

st.title("🚗 Automotive CAN Digital Dashboard")
st.markdown("### Simulated CAN Messages (IDs: 0x101, 0x102, 0x103)")

# Sidebar
st.sidebar.title("ECU Status")
st.sidebar.write("Engine ECU: ✅ Active")
st.sidebar.write("ABS ECU: ✅ Active")
st.sidebar.write("Battery ECU: ✅ Active")

# Layout
col1, col2, col3 = st.columns(3)

speed_placeholder = col1.empty()
rpm_placeholder = col2.empty()
temp_placeholder = col3.empty()

# ALWAYS RUN LOOP
while True:
    speed = random.randint(0, 120)
    rpm = random.randint(800, 5000)
    temp = random.randint(70, 110)

    speed_placeholder.metric("Speed (km/h)", speed)
    rpm_placeholder.metric("RPM", rpm)
    temp_placeholder.metric("Engine Temp (°C)", temp)

    time.sleep(1)