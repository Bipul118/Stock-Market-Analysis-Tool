def generate_signal(data):

    close = data["Close"].iloc[-1]
    ma50 = data["MA50"].iloc[-1]
    ma200 = data["MA200"].iloc[-1]


    if ma50 > ma200:
        return "BUY 🟢"

    else:
        return "SELL 🔴"
