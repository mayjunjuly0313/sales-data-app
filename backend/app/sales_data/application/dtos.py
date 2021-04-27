from typing import ClassVar
from pydantic import BaseModel

from sales_data.domain.repository import QueryParam


class GetBarChartDataInputDto(BaseModel):
    query_param: QueryParam


class GetBarChartDataOutputDto(BaseModel):
    bar_chart_data_json: str


class GetMinMaxProfitInputDto(BaseModel):
    query_param: QueryParam


class GetMinMaxProfitOutputDto(BaseModel):
    min_max_data: dict


class FailedOutputDto(BaseModel):
    SYSTEM_ERROR: ClassVar[str] = "System Error"

    type: str
    message: str

    @classmethod
    def build_system_error(cls, message: str = ""):
        return cls(type=cls.SYSTEM_ERROR, message=message)
