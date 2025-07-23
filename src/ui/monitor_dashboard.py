import streamlit as st
import requests
import time

st.title("Wayfinder Product Monitor")

with st.form("monitor_form"):
    url = st.text_input("Product URL", placeholder="https://www.disneystore.com/...")
    interval = st.number_input("Interval (seconds)", min_value=1, value=5)
    duration = st.number_input("Duration (seconds)", min_value=1, value=30)
    submitted = st.form_submit_button("Start Monitor")

if submitted:
    st.write("🚀 Starting monitor...")
    response = requests.post("http://localhost:8000/monitor", params={
        "url": url,
        "interval": interval,
        "duration": duration
    })

    if response.status_code == 200:
        job_id = response.json()["job_id"]
        st.success(f"Monitoring job started. Job ID: {job_id}")

        # Poll the results
        progress = st.empty()
        results_box = st.empty()
        start_time = time.time()

        while (time.time() - start_time) < duration:
            poll = requests.get(f"http://localhost:8000/monitor/{job_id}")
            if poll.status_code == 200:
                results = poll.json().get("results", [])
                results_box.json(results)
            time.sleep(interval)
        
        st.success("✅ Monitoring complete.")
    else:
        st.error("Failed to start monitoring job.")