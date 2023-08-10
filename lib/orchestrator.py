from .DataMaster import DataMaster
from .Designer import Designer
from typing import Optional, Literal


class Orchestrator:

    def __init__(self):
        print("Initializing Orchestrator...")
        print("Adding DataMaster...")
        self.dm = DataMaster()
        print("Adding Designer...")
        self.ds = Designer()

    def add_stock(
        self,
        ticker: str,
    ) -> None:
        self.dm.add_ticker(ticker=ticker)

    def remove_stock(
        self,
        ticker: str,
    ) -> None:
        self.dm.remove_ticker(ticker=ticker)

    def available_stocks(self) -> list:
        return self.dm.list_tickers()

    def plot_stock(
        self,
        ticker: str,
        period: Optional[Literal["1mo", "3mo", "6mo", "1y"]] = "3mo",
    ) -> None:
        data = self.dm.get_ticker_history(ticker=ticker, period=period)
        name = self.dm.get_ticker_info(ticker=ticker)["shortName"]
        self.ds.draw_plot(data, name)
        self.ds.save_plot(data, name)
