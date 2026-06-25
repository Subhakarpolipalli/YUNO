import streamlit as st
import pandas as pd

st.title("Yuno Fintech Strategy Dashboard")
st.write("Simulate transaction routing performance across regions.")

# User Input Controls
region = st.selectbox("Select Region", ["LATAM", "APAC", "EMEA"])
volume = st.slider("Daily Transaction Volume", 1000, 50000, 10000)

# Mock Calculation Logic
success_rate = 0.94 if region == "LATAM" else 0.97
successful_txns = int(volume * success_rate)

# Display Results
st.metric(label=f"Expected Successful Payments ({region})", value=successful_txns)
st.bar_chart(
    pd.DataFrame(
        {"Status": ["Success", "Failed"], "Count": [successful_txns, volume - successful_txns]}
    ).set_index("Status")
)
