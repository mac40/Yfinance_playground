from .DataMaster import DataMaster
from .Designer import Designer
from typing import Optional, Literal
from pandas import DataFrame


class Orchestrator:

    def __init__(self):
        print("Initializing Orchestrator...")
        print("Adding DataMaster...")
        self.__dm = DataMaster()
        print("Adding Designer...")
        self.__ds = Designer()

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
        self.__ds.draw_plot(data, name)
        self.__ds.save_plot(data, name)
