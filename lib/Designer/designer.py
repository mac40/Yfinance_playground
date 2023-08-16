import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.tsaplots import (
    plot_acf,
    plot_pacf,
)
from pandas import (
    DataFrame,
    Series,
)
from typing import Optional
from os import path


class Designer:
    def __init__(self):
        self.functions = {
            "plot": self.__plot,
            "series_plot": self.__series_plot,
            "multiseries_plot": self.__multiseries_plot,
            "auto_correlation": self.__plot_acf,
            "partial_auto_correlation": self.__plot_pacf,
            "prediction": self.__plot_prediction,
        }
        sns.set_theme(
            style="darkgrid",
            palette="muted",
        )

    def __series_plot(
        self,
        data: Series,
        name: Optional[str] = None,
    ) -> None:
        plt.subplots(figsize=(15, 5))
        sns.lineplot(data=data, label="Close", marker="s", color="b", markersize=1)

        plt.title(f"{name}")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True, alpha=0.5)

    def __multiseries_plot(
        self,
        data: list,
        name: Optional[str] = None,
    ) -> None:
        fig, axes = plt.subplots(len(data), figsize=(15, 5))
        for index, values in enumerate(data):
            axes[index].plot(values)

    def __plot(
        self,
        data: DataFrame,
        name: Optional[str] = None,
    ) -> None:
        # Line plot for Close prices
        plt.subplots(figsize=(15, 5))
        sns.lineplot(
            data=data["Close"], label="Close", marker="s", color="b", markersize=1
        )

        # Colored vertical lines for High-Low prices
        for index, row in data.iterrows():
            plt.vlines(
                index, row["Close"], row["High"], color="g", alpha=0.7, linewidth=2
            )
            plt.vlines(
                index, row["Low"], row["Close"], color="r", alpha=0.7, linewidth=2
            )

        plt.title(f"{name}")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True, alpha=0.5)

    def __plot_acf(
        self,
        data: Series,
        name: Optional[str] = None,
    ) -> None:
        fig, ax = plt.subplots(figsize=(15, 5))
        if name:
            plt.title(f"{name}")
        plot_acf(data, ax=ax)

    def __plot_pacf(
        self,
        data: Series,
        name: Optional[str] = None,
    ) -> None:
        fig, ax = plt.subplots(figsize=(15, 5))
        if name:
            plt.title(f"{name}")
        plot_pacf(data, ax=ax)

    def __plot_prediction(
        self,
        data: Series,
        prediction: Series,
        name: Optional[str] = None,
    ) -> None:
        plt.plot(data, color="b")
        plt.plot(prediction, color="r")

    def draw_plot(
        self,
        data: DataFrame,
        plot_type: str,
        name: Optional[str] = None,
        **kwargs,
    ) -> None:
        self.functions[plot_type](
            data=data,
            name=name,
            **kwargs,
        )
        plt.show()
        plt.close()

    def save_plot(
        self,
        data: DataFrame,
        plot_type: str,
        name: Optional[str] = None,
        **kwargs,
    ) -> None:
        self.functions[plot_type](
            data=data,
            name=name,
            **kwargs,
        )
        plt.savefig(path.join(path.dirname(__file__), f"Data/{name}.png"))
        plt.close()
