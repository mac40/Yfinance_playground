from statsmodels.tsa.stattools import adfuller
from pandas import Series


class DataScientist:

    def __init__(self):
        self.knowledgebase = {}

    def print_adfuller(
        self,
        data: Series,
    ) -> None:
        result = adfuller(data)
        print('ADF Statistic: %f' % result[0])
        print('p-value: %f' % result[1])
        print('Critical Values:')
        for key, value in result[4].items():
            print('\t%s: %.3f' % (key, value))

    def differenciate_data(
        self,
        data: Series,
        diff_lvl: int,
    ) -> Series:
        for _ in range(diff_lvl):
            data = data.diff()
        return data
