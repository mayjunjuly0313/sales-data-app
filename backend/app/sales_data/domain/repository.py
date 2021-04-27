from abc import ABCMeta, abstractmethod
from typing import TypeVar
from pydantic import BaseModel

PandasDataFrame = TypeVar("pandas.core.frame.DataFrame")


class QueryParam(BaseModel):
    data_form: str


class SalesDataRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_bar_chart_data(self, query_param: QueryParam) -> PandasDataFrame:
        pass

    @abstractmethod
    def get_min_max_data(self, query_param: QueryParam) -> str:
        pass

    @abstractmethod
    def set_chart_data(self, chart_data: PandasDataFrame, data_form: str, chart_type: str) -> None:
        pass

    @abstractmethod
    def set_min_max_data(self, data_form: str, max_profit: str, min_profit: str) -> None:
        pass
