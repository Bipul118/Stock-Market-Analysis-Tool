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
            .ewm(span=20, adjust=False)
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


        mid = (
            data["Close"]
            .rolling(20)
            .mean()
        )


        std = (
            data["Close"]
            .rolling(20)
            .std()
        )


        data["BB_UPPER"] = mid + (2 * std)

        data["BB_LOWER"] = mid - (2 * std)




    # MACD
    if "MACD" in selected:


        ema12 = (
            data["Close"]
            .ewm(
                span=12,
                adjust=False
            )
            .mean()
        )


        ema26 = (
            data["Close"]
            .ewm(
                span=26,
                adjust=False
            )
            .mean()
        )


        data["MACD"] = ema12 - ema26


        data["MACD_SIGNAL"] = (
            data["MACD"]
            .ewm(
                span=9,
                adjust=False
            )
            .mean()
        )



    return data