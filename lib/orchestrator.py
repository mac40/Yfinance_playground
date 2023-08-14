from .DataMaster import DataMaster
from .Designer import Designer
from .DataScientist import DataScientist
from typing import Optional, Literal
from pandas import DataFrame


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

    def plot_autocorrelation(
        self,
        ticker: str,
        max_lags: int = 20,
        period: Optional[Literal["1mo", "3mo", "6mo", "1y"]] = "3mo",
    ) -> None:
        name = self.__dm.get_ticker_info(ticker=ticker)["shortName"]
        data = self.__dm.get_ticker_history(ticker=ticker, period=period)["Close"]
        self.__des.draw_plot(data=data, plot_type="auto_correlation", name=name, max_lags=max_lags)

    def print_adfuller(
        self,
        ticker: str,
        period: Optional[Literal["1mo", "3mo", "6mo", "1y"]] = "3mo",
    ) -> None:
        data = self.__dm.get_ticker_history(ticker=ticker, period=period)["Close"]
        self.__ds.print_adfuller(data=data)

    def plot_diff_data(
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
