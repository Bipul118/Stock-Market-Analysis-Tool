def add_indicators(data):


    close = data["Close"]


    data["MA50"] = (
        close
        .rolling(50)
        .mean()
    )


    data["MA200"] = (
        close
        .rolling(200)
        .mean()
    )


    delta = close.diff()


    gain = (
        delta.where(delta > 0, 0)
        .rolling(14)
        .mean()
    )


    loss = (
        -delta.where(delta < 0, 0)
        .rolling(14)
        .mean()
    )


    rs = gain / loss


    data["RSI"] = (
        100 - (100/(1+rs))
    )


    return data