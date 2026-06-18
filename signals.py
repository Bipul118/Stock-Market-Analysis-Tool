def generate_signal(data):

    latest_ma50 = float(data["MA50"].iloc[-1])
    latest_ma200 = float(data["MA200"].iloc[-1])


    if latest_ma50 > latest_ma200:

        return "BUY 🟢"


    elif latest_ma50 < latest_ma200:

        return "SELL 🔴"


    else:

        return "HOLD 🟡"