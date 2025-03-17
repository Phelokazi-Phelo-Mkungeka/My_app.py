import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

st.title("Random Time Series Generator")

# Session state to store data
if 'time_series_data' not in st.session_state:
    st.session_state.time_series_data = None
    st.session_state.graph_generated = False

def generate_time_series():
    dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
    values = np.cumsum(np.random.randn(100))  # Random walk
    df = pd.DataFrame({'Date': dates, 'Value': values})
    return df

# Generate graph button
if st.button("Generate Time Series Graph"):
    st.session_state.time_series_data = generate_time_series()
    st.session_state.graph_generated = True

# Display graph if data exists
if st.session_state.graph_generated and st.session_state.time_series_data is not None:
    fig, ax = plt.subplots()
    ax.plot(st.session_state.time_series_data['Date'], st.session_state.time_series_data['Value'])
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.set_title("Random Time Series")
    st.pyplot(fig)

    # Download button
    csv = st.session_state.time_series_data.to_csv(index=False)
    st.download_button("Download CSV", csv, "time_series.csv", "text/csv")
