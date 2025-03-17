import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io

st.title("This is a test app")
st.write("This is a simulation for a random time series graph.")

# Session state to track button clicks
if 'data' not in st.session_state:
    st.session_state.data = None
if 'button_one_clicked' not in st.session_state:
    st.session_state.button_one_clicked = False

def generate_time_series():
    """Generate a random time series dataset."""
    timestamps = pd.date_range(start=pd.Timestamp.now(), periods=50, freq='H')
    values = np.random.randn(50).cumsum()
    df = pd.DataFrame({'Timestamp': timestamps, 'Value': values})
    return df

if st.button("Generate Time Series"):
    st.session_state.data = generate_time_series()
    st.session_state.button_one_clicked = True
    st.experimental_rerun()

if st.session_state.button_one_clicked and st.session_state.data is not None:
    st.line_chart(st.session_state.data.set_index("Timestamp"))
    
    csv = st.session_state.data.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="time_series_data.csv",
        mime="text/csv"
    )
