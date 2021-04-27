from dependency_injector.wiring import inject, Provide
from flask import request
from flask_cors import cross_origin

from container import Container
from sales_data.application.dtos import GetBarChartDataInputDto, GetMinMaxProfitInputDto
from sales_data.application.service import SalesDataApplicationService
from sales_data.domain.repository import QueryParam


# query param = form : "products_profit_by_regions" or "regions_profit_by_products"
@cross_origin()
@inject
def get_chart_data(
    sales_data_application_service: SalesDataApplicationService = Provide[Container.sales_data_application_service],
):
    query_param = QueryParam(data_form=request.args.get("form"))
    input_dto = GetBarChartDataInputDto(query_param=query_param)
    output_dto = sales_data_application_service.get_bar_chart_data(input_dto=input_dto)
    print(output_dto.bar_chart_data_json)
    return output_dto.bar_chart_data_json, 200


# query param = form : "products_profit_by_regions" or "regions_profit_by_products"
@cross_origin()
@inject
def get_min_max_profit_data(
    sales_data_application_service: SalesDataApplicationService = Provide[Container.sales_data_application_service],
):
    query_param = QueryParam(data_form=request.args.get("form"))
    input_dto = GetMinMaxProfitInputDto(query_param=query_param)
    output_dto = sales_data_application_service.get_min_max_profit(input_dto=input_dto)
    print(output_dto)
    return output_dto.min_max_data, 200


@cross_origin()
@inject
def health_check():
    return {"msg": "I am Healthy!"}, 200