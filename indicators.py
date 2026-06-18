import pandas as pd


def add_indicators(data, selected):

    # SMA
    if "SMA 20" in selected:
        data["SMA20"] = (
            data["Close"]
            .rolling(20)
            .mean()
        )


    # EMA
    if "EMA 20" in selected:
        data["EMA20"] = (
            data["Close"]
            .ewm(span=20)
            .mean()
        )


    # RSI
    if "RSI" in selected:

        delta = data["Close"].diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(14).mean()
        avg_loss = loss.rolling(14).mean()

        rs = avg_gain / avg_loss

        data["RSI"] = 100 - (
            100 / (1 + rs)
        )


    # Bollinger Band

    if "Bollinger Band" in selected:

        data["BB_MID"] = (
            data["Close"]
            .rolling(20)
            .mean()
        )

        std = (
            data["Close"]
            .rolling(20)
            .std()
        )

        data["BB_UPPER"] = (
            data["BB_MID"] + 2*std
        )

        data["BB_LOWER"] = (
            data["BB_MID"] - 2*std
        )


    return data