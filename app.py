import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from data_fetch import get_stock_data
from indicators import add_indicators
from signals import generate_signal
from prediction import predict_price


st.set_page_config(
    page_title="Stock Analysis Tool",
    layout="wide"
)


st.title("📈 AI Stock Market Analysis Tool")


# -------------------------
# Stock Dropdown
# -------------------------

stocks = {
    "Reliance": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS",
    "SBI": "SBIN.NS"
}


selected = st.selectbox(
    "Select Stock",
    list(stocks.keys())
)


symbol = stocks[selected]


# -------------------------
# Data
# -------------------------

data = get_stock_data(symbol)

data = add_indicators(data)


signal = generate_signal(data)

prediction = predict_price(data)



# -------------------------
# Metrics
# -------------------------

col1,col2,col3 = st.columns(3)


col1.metric(
    "Current Price",
    round(data["Close"].iloc[-1],2)
)


col2.metric(
    "Signal",
    signal
)


col3.metric(
    "Prediction",
    round(prediction,2)
)



# -------------------------
# Chart
# -------------------------

fig = go.Figure()


fig.add_trace(
    go.Scatter(
        x=data.index,
        y=data["Close"],
        name="Price"
    )
)


fig.add_trace(
    go.Scatter(
        x=data.index,
        y=data["MA50"],
        name="MA50"
    )
)


fig.add_trace(
    go.Scatter(
        x=data.index,
        y=data["MA200"],
        name="MA200"
    )
)


st.plotly_chart(fig)



# -------------------------
# RSI
# -------------------------

st.subheader("RSI")

st.line_chart(
    data["RSI"]
)



# -------------------------
# Portfolio Tracker
# -------------------------

st.header("💼 Portfolio Tracker")


shares = st.number_input(
    "Number of Shares",
    min_value=1,
    value=10
)


buy_price = st.number_input(
    "Buy Price",
    min_value=1.0,
    value=1000.0
)


current = float(
    data["Close"].iloc[-1]
)


profit = (
    current - buy_price
) * shares


st.metric(
    "Profit / Loss",
    round(profit,2)
)