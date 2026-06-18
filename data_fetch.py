import yfinance as yf


def get_stock_data(symbol):

    data = yf.download(
        symbol,
        period="1y",
        auto_adjust=False
    )


    # Fix yfinance MultiIndex
    if hasattr(data.columns, "levels"):

        data.columns = data.columns.get_level_values(0)


    return data