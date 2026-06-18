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
    "Reliance": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS",
    "SBI": "SBIN.NS",
    "ITC": "ITC.NS",
    "Adani Enterprises": "ADANIENT.NS",
    "Adani Ports": "ADANIPORTS.NS",
    "Larsen & Toubro": "LT.NS",
    "HUL": "HINDUNILVR.NS",
    "Maruti": "MARUTI.NS",
    "Bajaj Finance": "BAJFINANCE.NS",
    "Axis Bank": "AXISBANK.NS",
    "Kotak Bank": "KOTAKBANK.NS",
    "Wipro": "WIPRO.NS",
    "HCL Tech": "HCLTECH.NS",
    "Tech Mahindra": "TECHM.NS",
    "Sun Pharma": "SUNPHARMA.NS",
    "Tata Motors": "TATAMOTORS.NS",
    "Tata Steel": "TATASTEEL.NS",
    "Power Grid": "POWERGRID.NS",
    "NTPC": "NTPC.NS",
    "ONGC": "ONGC.NS",
    "Coal India": "COALINDIA.NS",
    "Bharti Airtel": "BHARTIARTL.NS"

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
        "MACD"
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
# MACD

if "MACD" in selected:


    macd_fig = go.Figure()


    macd_fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["MACD"],
            name="MACD"
        )
    )


    macd_fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["MACD_SIGNAL"],
            name="Signal Line"
        )
    )


    st.subheader("MACD")


    st.plotly_chart(
        macd_fig,
        use_container_width=True
    )
# ----------------
# Volume Chart
# ----------------

st.subheader("Volume")


volume_fig = go.Figure()


volume_fig.add_trace(

    go.Bar(

        x=data.index,

        y=data["Volume"],

        name="Volume"

    )

)


volume_fig.update_layout(
    height=300
)


st.plotly_chart(
    volume_fig,
    use_container_width=True
)


# RSI

if "RSI" in selected:

    st.subheader("RSI")

    st.line_chart(
        data["RSI"]
    )