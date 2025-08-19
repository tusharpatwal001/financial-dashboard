import streamlit as st
from datetime import datetime, timedelta
from src.data_ingestion import get_data
from src.data_processing import add_moving_average, add_macd, add_bollinger_bands, add_rsi
from src.plots import plot_price, plot_volume, plot_macd, plot_rsi
import yfinance as yf
import pandas as pd

# ---------------------------
# Streamlit App
# ---------------------------
st.set_page_config(page_title="Pro Stock Dashboard", layout="wide")

st.title("📊 Pro Stock Dashboard")

# Sidebar controls
st.sidebar.header("Settings")
ticker = st.sidebar.text_input("Enter Ticker Symbol", value="AAPL")
start_date = st.sidebar.date_input(
    "Start Date", value=datetime.today() - timedelta(days=365))
end_date = st.sidebar.date_input("End Date", value=datetime.today())
ma_window = st.sidebar.slider(
    "Moving Avg Window (days)", min_value=5, max_value=60, value=10)

# Load and Process Data
df = get_data(ticker, start_date, end_date)

if not df.empty:
    df = add_moving_average(df, window=ma_window)
    df = add_bollinger_bands(df)
    df = add_rsi(df)
    df = add_macd(df)

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📈 Price", "📊 Volume", "📉 RSI", "📉 MACD"])

    with tab1:
        st.plotly_chart(plot_price(df, ticker), use_container_width=True)

    with tab2:
        st.plotly_chart(plot_volume(df, ticker), use_container_width=True)

    with tab3:
        st.plotly_chart(plot_rsi(df, ticker), use_container_width=True)

    with tab4:
        st.plotly_chart(plot_macd(df, ticker), use_container_width=True)

    # Show raw data
    st.subheader("Raw Data")
    st.dataframe(df)

    # Download CSV
    csv = df.to_csv().encode('utf-8')
    st.download_button(
        label="⬇️ Download Data as CSV",
        data=csv,
        file_name=f"{ticker}_data.csv",
        mime="text/csv",
    )
else:
    st.warning("⚠️ No data found for the selected ticker and date range.")
