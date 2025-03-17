import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Random Time Series Generator")

# Initialize session state for storing the time series data
if "time_series_data" not in st.session_state:
    st.session_state.time_series_data = None
    st.session_state.graph_generated = False

# Function to generate random time series data
def generate_time_series():
    dates = pd.date_range(start="2023-01-01", periods=100, freq="D")
    values = np.cumsum(np.random.randn(100))  # Creates a random walk series
    df = pd.DataFrame({"Date": dates, "Value": values})
    return df

# Button to generate the graph
if st.button("Generate Time Series Graph"):
    st.session_state.time_series_data = generate_time_series()
    st.session_state.graph_generated = True

# Display the graph if data exists
if st.session_state.graph_generated and st.session_state.time_series_data is not None:
    fig, ax = plt.subplots(figsize=(10, 5))  # Added figsize for better visibility
    ax.plot(
        st.session_state.time_series_data["Date"],
        st.session_state.time_series_data["Value"],
        marker="o",
        linestyle="-",
        color="b",
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.set_title("Random Time Series Graph")
    ax.grid(True)  # Adds grid for better readability
    st.pyplot(fig)  # Display the graph

    # Convert DataFrame to CSV
    csv_data = st.session_state.time_series_data.to_csv(index=False).encode("utf-8")
    
    # Download button
    st.download_button(
        label="Download CSV",
        data=csv_data,
        file_name="time_series.csv",
        mime="text/csv",
    )
