from .DataMaster import DataMaster
from .Designer import Designer
from .DataScientist import DataScientist
from typing import Optional, Literal
from pandas import DataFrame
import matplotlib.pyplot as plt


class Orchestrator:

    def __init__(self):
        print("Initializing Orchestrator...")
        print("Adding DataMaster...")
        self.__dm = DataMaster()
        print("Adding Designer...")
        self.__des = Designer()
        print("Adding DataScientist...")
        self.__ds = DataScientist()

    def add_stock(
        self,
        ticker: str,
    ) -> None:
        self.__dm.add_ticker(ticker=ticker)

    def remove_stock(
        self,
        ticker: str,
    ) -> None:
        self.__dm.remove_ticker(ticker=ticker)

    def available_stocks(self) -> list:
        return self.__dm.list_tickers()

    def get_stock_history(
        self,
        ticker: str,
        period: Optional[Literal["1mo", "3mo", "6mo", "1y"]] = "3mo",
    ) -> DataFrame:
        return self.__dm.get_ticker_history(ticker=ticker, period=period)

    def plot_stock(
        self,
        ticker: str,
        period: Optional[Literal["1mo", "3mo", "6mo", "1y"]] = "3mo",
    ) -> None:
        data = self.__dm.get_ticker_history(ticker=ticker, period=period)
        name = self.__dm.get_ticker_info(ticker=ticker)["shortName"]
        self.__des.draw_plot(data=data, plot_type="plot", name=name)
        self.__des.save_plot(data=data, plot_type="plot", name=name)

    def print_adfuller(
        self,
        ticker: str,
        period: Optional[Literal["1mo", "3mo", "6mo", "1y"]] = "3mo",
        diff_level: Optional[int] = None,
    ) -> None:
        data = self.__dm.get_ticker_history(ticker=ticker, period=period)["Close"]
        if diff_level:
            data = self.__ds.differenciate_data(data=data, diff_lvl=diff_level)
        result = self.__ds.adfuller(data=data)
        print('ADF Statistic: %f' % result[0])
        print('p-value: %f' % result[1])
        print('Critical Values:')
        for key, value in result[4].items():
            print('\t%s: %.3f' % (key, value))

    def plot_diffs_stock(
        self,
        ticker: str,
        period: Optional[Literal["1mo", "3mo", "6mo", "1y"]] = "3mo",
        diff_levels: int = 2,
    ) -> None:
        data = self.__dm.get_ticker_history(ticker=ticker, period=period)["Close"]
        diffs = []
        diffs.append(data)
        for i in range(diff_levels):
            diffs.append(self.__ds.differenciate_data(data=data, diff_lvl=i + 1))
        self.__des.draw_plot(data=diffs, plot_type="multiseries_plot")

    def plot_acf(
        self,
        ticker: str,
        period: Optional[Literal["1mo", "3mo", "6mo", "1y"]] = "3mo",
        diff_level: Optional[int] = None,
    ) -> None:
        name = self.__dm.get_ticker_info(ticker=ticker)["shortName"]
        data = self.__dm.get_ticker_history(ticker=ticker, period=period)["Close"]
        if diff_level:
            data = self.__ds.differenciate_data(data=data, diff_lvl=diff_level)
        self.__des.draw_plot(data=data, plot_type="auto_correlation", name=name)

    def plot_pacf(
        self,
        ticker: str,
        period: Optional[Literal["1mo", "3mo", "6mo", "1y"]] = "3mo",
        diff_level: Optional[int] = None,
    ) -> None:
        name = self.__dm.get_ticker_info(ticker=ticker)["shortName"]
        data = self.__dm.get_ticker_history(ticker=ticker, period=period)["Close"]
        if diff_level:
            data = self.__ds.differenciate_data(data=data, diff_lvl=diff_level)
        self.__des.draw_plot(data=data, plot_type="partial_auto_correlation", name=name)

    def test_model(
        self,
        ticker: str,
        p: int,
        q: int,
        d: int,
        period: Optional[Literal["1mo", "3mo", "6mo", "1y"]] = "3mo",
    ) -> None:
        data = self.__dm.get_ticker_history(ticker=ticker, period=period)["Close"]
        test, predictions = self.__ds.test_arima(data, p, q, d)
        self.__des.draw_plot(plot_type="prediction", data=test, prediction=predictions)

    def predict(
        self,
        ticker: str,
        p: int,
        q: int,
        d: int,
        period: Optional[Literal["1mo", "3mo", "6mo", "1y"]] = "3mo",
        future: Literal[5, 10, 20, 30] = 10,
    ) -> None:
        data = self.__dm.get_ticker_history(ticker=ticker, period=period)["Close"]
        fitted, predictions = self.__ds.predict_arima(data=data, p=p, q=q, d=d, period=future)
        forecast = [x for x in fitted] + [x for x in predictions]
        self.__des.draw_plot(data=data.values[2:], plot_type="prediction", prediction=forecast[2:])
