from statsmodels.tsa.stattools import adfuller
from statsmodels.tools.sm_exceptions import ConvergenceWarning
import warnings
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import (
    ARIMA,
    ARIMAResults,
)
from pandas import Series
from typing import Literal


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

    def __test_model(
        self,
        data: Series,
        order: tuple,
    ) -> int:
        train_size = int(len(data) * 0.66)
        train, test = data[0:train_size], data[train_size:]
        history = [x for x in train]
        # make predictions
        predictions = list()
        for t in range(len(test)):
            model = ARIMA(history, order=order)
            model.initialize_approximate_diffuse()
            model_fit = model.fit()
            yhat = model_fit.forecast()[0]
            predictions.append(yhat)
            history.append(test[t])
        # calculate out of sample error
        error = mean_squared_error(test, predictions)
        return error

    def evaluate_hyperparameters(
        self,
        data: Series,
        p_values: list,
        d_values: range,
        q_values: range,
    ) -> (tuple, int):
        data = data.values.astype('float32')
        best_score, best_cfg = float("inf"), None
        warnings.simplefilter('ignore', ConvergenceWarning)
        for p in p_values:
            for d in d_values:
                for q in q_values:
                    order = (p, d, q)
                    try:
                        mse = self.__test_model(data, order)
                        if mse < best_score:
                            best_score, best_cfg = mse, order
                        print('ARIMA%s MSE=%.3f' % (order, mse))
                    except ConvergenceWarning:
                        continue
        return best_cfg, best_score

    def test_arima(
        self,
        data: Series,
        p: int,
        q: int,
        d: int,
        test_size: int = 30,
    ) -> (list, list):
        X = data.values
        size = int(len(X) - test_size)
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
