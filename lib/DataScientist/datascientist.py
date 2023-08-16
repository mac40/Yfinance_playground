from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import (
    ARIMA,
    ARIMAResults,
)
from pandas import Series
from math import sqrt
from typing import Literal
from sklearn.metrics import mean_squared_error


class DataScientist:

    def __init__(self):
        self.knowledgebase = {}

    def adfuller(
        self,
        data: Series,
    ) -> None:
        return adfuller(data)

    def differenciate_data(
        self,
        data: Series,
        diff_lvl: int,
    ) -> Series:
        for _ in range(diff_lvl):
            data = data.diff()
        return data.dropna()

    def test_arima(
        self,
        data: Series,
        p: int,
        q: int,
        d: int,
    ) -> (list, list):
        X = data.values
        size = int(len(X) - 30)
        train, test = X[0:size], X[size:len(X)]
        model = ARIMA(train, order=(p, q, d))
        model_fit: ARIMAResults = model.fit()
        fitted = model_fit.fittedvalues
        predictions = model_fit.forecast(steps=len(test))
        return fitted, predictions

    def predict_arima(
        self,
        data: Series,
        p: int,
        d: int,
        q: int,
        period: Literal[5, 10, 20, 30] = 15
    ) -> list:
        model = ARIMA(data.values, order=(p, q, d))
        model_fit: ARIMAResults = model.fit()
        fitted = model_fit.fittedvalues
        predictions = model_fit.forecast(steps=period)
        return fitted, predictions
