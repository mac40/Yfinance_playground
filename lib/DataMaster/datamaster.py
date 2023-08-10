from pandas import DataFrame
from typing import Literal, Optional
from yfinance import Ticker
from pickle import dump, load
from os import listdir, path
from inspect import currentframe, getouterframes
from .decorators import getter


class DataMaster:

    def __init__(self):
        self.ticker_dict = {}
        self.__read_watchlist()

    def add_ticker(
        self,
        ticker: str,
    ) -> None:
        if ticker not in self.list_tickers():
            new_ticker = Ticker(ticker)
            self.ticker_dict[ticker] = new_ticker
            if getouterframes(currentframe(), 2)[1][3] != "__read_watchlist":
                self.__serialize_watchlist()
        else:
            print("Ticker already in list")

    def remove_ticker(
        self,
        ticker: str,
    ) -> None:
        if ticker not in self.list_tickers():
            return
        self.ticker_dict.pop(ticker)
        self.__serialize_watchlist()

    def list_tickers(
        self,
    ) -> list:
        return list(self.ticker_dict.keys())

    @getter
    def get_ticker_info(
        self,
        ticker: str,
    ) -> str:
        return self.ticker_dict[ticker].info

    @getter
    def get_ticker_history(
        self,
        ticker: str,
        period: Optional[Literal["1mo", "3mo", "6mo", "1y"]] = None,
    ) -> DataFrame:
        return self.ticker_dict[ticker].history(period=period)

    def update_memory(self):
        self.__serialize_watchlist()

    def __serialize_watchlist(self):
        with open(path.join(path.dirname(__file__), "Data/tickers.pkl"), "wb") as f:
            dump(self.list_tickers(), f)

    def __read_watchlist(self):
        if "tickers.pkl" in listdir(path.join(path.dirname(__file__), "Data")):
            with open(path.join(path.dirname(__file__), "Data/tickers.pkl"), "rb") as f:
                tickers_list = load(f)
                for ticker in tickers_list:
                    self.add_ticker(ticker)
