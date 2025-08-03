import streamlit as st
from data_preprocessing import load_and_prepare_data
from forecasting import generate_forecast
from utils import filter_data
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="Hotel Revenue Forecast Dashboard")

st.title("📈 Hotel Revenue & Occupancy Forecast")

# Load Data
df = load_and_prepare_data()

# Sidebar Filters
hotel_type = st.sidebar.selectbox("Hotel Type", df['hotel'].unique())
room_type = st.sidebar.selectbox("Room Type", df['reserved_room_type'].unique())
customer_type = st.sidebar.selectbox("Customer Type", df['customer_type'].unique())

# Filtered Data
filtered_df = filter_data(df, hotel_type, room_type, customer_type)

# Forecasting
forecast = generate_forecast(filtered_df, target="adr", periods=30)

# Plot Forecast
fig = go.Figure()
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='Forecast'))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], name='Upper', line=dict(dash='dash')))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], name='Lower', line=dict(dash='dash')))
st.plotly_chart(fig, use_container_width=True)
