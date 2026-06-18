import streamlit as st
import plotly.graph_objects as go


from data_fetch import get_stock_data
from indicators import add_indicators
from signals import generate_signal



st.set_page_config(
    page_title="Mini TradingView",
    layout="wide"
)


st.title("📈 Mini TradingView Stock Analyzer")


# ----------------
# Stock
# ----------------

stocks = {
    "Reliance":"RELIANCE.NS",
    "TCS":"TCS.NS",
    "Infosys":"INFY.NS",
    "HDFC Bank":"HDFCBANK.NS",
    "SBI":"SBIN.NS"
}


choice = st.selectbox(
    "Select Stock",
    list(stocks.keys())
)


symbol = stocks[choice]



# ----------------
# Indicators
# ----------------


selected = st.multiselect(

    "Select Indicators",

    [
        "SMA 20",
        "EMA 20",
        "RSI",
        "Bollinger Band"
    ]

)



# ----------------
# Data
# ----------------

data = get_stock_data(symbol)


# MA for signal

data["MA50"] = (
    data["Close"]
    .rolling(50)
    .mean()
)


data["MA200"] = (
    data["Close"]
    .rolling(200)
    .mean()
)



data = add_indicators(
    data,
    selected
)



signal = generate_signal(data)


st.subheader(
    f"Signal : {signal}"
)



# ----------------
# Candle Chart
# ----------------


fig = go.Figure()


fig.add_trace(

    go.Candlestick(

        x=data.index,

        open=data["Open"],

        high=data["High"],

        low=data["Low"],

        close=data["Close"],

        name="Price"

    )

)



# SMA

if "SMA 20" in selected:

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["SMA20"],
            name="SMA20"
        )
    )



# EMA

if "EMA 20" in selected:

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["EMA20"],
            name="EMA20"
        )
    )



# Bollinger

if "Bollinger Band" in selected:


    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["BB_UPPER"],
            name="BB Upper"
        )
    )


    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["BB_LOWER"],
            name="BB Lower"
        )
    )



st.plotly_chart(
    fig,
    use_container_width=True
)



# RSI

if "RSI" in selected:

    st.subheader("RSI")

    st.line_chart(
        data["RSI"]
    )