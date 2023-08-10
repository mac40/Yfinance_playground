import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame
from typing import Optional
from os import listdir, path


class Designer:

    def __init__(self):
        sns.set_theme(
            style="darkgrid",
            palette="muted",
        )

    def plot(
        self,
        data: DataFrame,
        name: Optional[str] = None,
    ) -> plt:
        # Line plot for Close prices
        plt.subplots(figsize=(15, 5))
        sns.lineplot(data=data['Close'], label='Close', marker='s', color="b", markersize=1)

        # Colored vertical lines for High-Low prices
        for index, row in data.iterrows():
            plt.vlines(index, row['Close'], row['High'], color="g", alpha=0.7, linewidth=2)
            plt.vlines(index, row['Low'], row['Close'], color="r", alpha=0.7, linewidth=2)

        plt.title(f'{name}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True, alpha=0.5)
        return plt

    def draw_plot(
        self,
        data: DataFrame,
        name: Optional[str] = None,
    ) -> None:
        plt = self.plot(
            data=data,
            name=name,
        )
        plt.show()

    def save_plot(
        self,
        data: DataFrame,
        name: Optional[str] = None,
    ) -> None:
        plt = self.plot(
            data=data,
            name=name,
        )
        plt.savefig(path.join(path.dirname(__file__), f"Data/{name}.png"))
