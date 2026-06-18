from sklearn.linear_model import LinearRegression
import numpy as np


def predict_price(data):

    df = data.copy()


    df["Target"] = df["Close"].shift(-1)


    df = df.dropna()


    X = df[["Close", "MA50", "MA200"]]

    y = df["Target"]


    model = LinearRegression()

    model.fit(X, y)


    latest = np.array(
        [[
            data["Close"].iloc[-1],
            data["MA50"].iloc[-1],
            data["MA200"].iloc[-1]
        ]]
    )


    prediction = model.predict(latest)


    return prediction[0]