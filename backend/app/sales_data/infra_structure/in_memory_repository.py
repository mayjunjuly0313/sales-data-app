from sales_data.application.dtos import QueryParam
from sales_data.domain.repository import SalesDataRepository
from typing import TypeVar, Tuple

PandasDataFrame = TypeVar("pandas.core.frame.DataFrame")


class InMemorySalesDataRepository(SalesDataRepository):
    def __init__(self):
        self.data_form_to_data = {}
        self.data_form_to_min_max = {}

    def get_bar_chart_data(self, query_param: QueryParam) -> PandasDataFrame:
        return self.data_form_to_data[("bar", query_param.data_form)]

    def get_min_max_data(self, query_param: QueryParam) -> Tuple:
        return self.data_form_to_min_max[query_param.data_form]

    def set_chart_data(self, chart_data: PandasDataFrame, data_form: str, chart_type: str) -> None:
        self.data_form_to_data[(chart_type, data_form)] = chart_data

    def set_min_max_data(self, data_form: str, max_profit: str, min_profit: str) -> None:
        self.data_form_to_min_max[data_form] = ({"min": min_profit}, {"max": max_profit})
