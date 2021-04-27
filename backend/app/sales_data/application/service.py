import pandas as pd
from sales_data.application.dtos import (
    GetBarChartDataInputDto,
    GetBarChartDataOutputDto,
    GetMinMaxProfitInputDto,
    GetMinMaxProfitOutputDto,
    FailedOutputDto,
)
from sales_data.domain.repository import SalesDataRepository
import numpy as np
from typing import TypeVar, List, Union

PandasDataFrame = TypeVar("pandas.core.frame.DataFrame")


class SalesDataApplicationService:
    def __init__(self, sales_data_repository=SalesDataRepository) -> None:
        self.sales_data_repository = sales_data_repository

    def get_bar_chart_data(
        self, input_dto: GetBarChartDataInputDto
    ) -> Union[GetBarChartDataOutputDto, FailedOutputDto]:
        try:
            bar_chart_df = self.sales_data_repository.get_bar_chart_data(input_dto.query_param)

            # match with the data format of chart library
            bar_chart_df = bar_chart_df.reset_index()
            bar_chart_data_json = bar_chart_df.to_json(orient="records")

            return GetBarChartDataOutputDto(bar_chart_data_json=bar_chart_data_json)
        except Exception as e:
            return FailedOutputDto.build_system_error(message=str(e))

    def get_min_max_profit(
        self, input_dto: GetMinMaxProfitInputDto
    ) -> Union[GetMinMaxProfitOutputDto, FailedOutputDto]:
        try:
            min_max_profit_data = self.sales_data_repository.get_min_max_data(input_dto.query_param)
            min_profit_data = min_max_profit_data[0]["min"]
            max_profit_data = min_max_profit_data[1]["max"]

            return GetMinMaxProfitOutputDto(min_max_data={"min": min_profit_data, "max": max_profit_data})
        except Exception as e:
            return FailedOutputDto.build_system_error(message=str(e))

    def set_initial_data(self, file_name: str) -> None:
        try:
            _sales_dataframe = pd.read_csv(file_name)
            _sales_dataframe = _sales_dataframe[["Region", "Item Type", "Total Profit"]]
            _sales_dataframe = _sales_dataframe.groupby(["Region", "Item Type"]).sum()
            products_profit_by_regions_df = _sales_dataframe.unstack(-1)
            regions_profit_by_products_df = _sales_dataframe.unstack(0)

            # columns
            products = [
                "Baby Food",
                "Beverages",
                "Cereal",
                "Clothes",
                "Cosmetics",
                "Fruits",
                "Household",
                "Meat",
                "Office Supplies",
                "Personal Care",
                "Snacks",
                "Vegetables",
            ]
            regions = [
                "Asia",
                "Australia and Oceania",
                "Central America and the Caribbean",
                "Europe",
                "Middle East and North Africa",
                "North America",
                "Sub-Saharan Africa",
            ]

            self.set_bar_chart_data(
                dataframe=products_profit_by_regions_df,
                columns=products,
                data_form="products_profit_by_regions",
                chart_type="bar",
            )
            self.set_bar_chart_data(
                dataframe=regions_profit_by_products_df,
                columns=regions,
                data_form="regions_profit_by_products",
                chart_type="bar",
            )
        except Exception as e:
            print(str(e))

    def set_bar_chart_data(self, dataframe: PandasDataFrame, columns: List, data_form: str, chart_type: str):
        try:
            dataframe.columns = columns
            dataframe["Total Profit"] = dataframe.apply(np.sum, axis=1)

            # set min and max data
            max_profit = dataframe["Total Profit"].idxmax()
            min_profit = dataframe["Total Profit"].idxmin()
            self.sales_data_repository.set_min_max_data(
                data_form=data_form, max_profit=max_profit, min_profit=min_profit
            )

            self.sales_data_repository.set_chart_data(chart_data=dataframe, data_form=data_form, chart_type=chart_type)
        except Exception as e:
            print(str(e))
