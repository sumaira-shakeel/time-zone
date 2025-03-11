import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONES = [
        "UTC",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "Africa/Johannesburg",
    "Asia/Karachi",
    "America/Los_Angeles",
    "Europe/Paris",
    "Asia/Dubai",
    "Asia/Kolkata",
]

st.title("Time Zone App")

selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC","Asia/Karachi"])

st.subheader("Selected Time Zone")

for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%y-%m-%d   %I   %H:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")

st.subheader("Covert Time Between Timezones")

current_time = st.time_input(" Current Time", value=datetime.now().time())
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%y-%m-%d   %I   %H:%M:%S %p")
    st.success(f"Converted Time in {to_tz}: {converted_time}")


