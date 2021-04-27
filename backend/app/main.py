import sys
from flask import Flask
from flask_cors import CORS

from container import Container
from dependency_injector.wiring import inject, Provide
from sales_data.application.service import SalesDataApplicationService
from sales_data.external_interface.routers import get_chart_data, get_min_max_profit_data, health_check

csv_file = "Sales Records - Evaluation.csv"


@inject
def data_setup(
    sales_data_application_service: SalesDataApplicationService = Provide[Container.sales_data_application_service],
):
    sales_data_application_service.set_initial_data(file_name=csv_file)


def create_app() -> Flask:
    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    app = Flask(__name__)
    CORS(app)
    app.container = container
    app.before_first_request(data_setup)
    app.add_url_rule("/health", "health_check", health_check)
    app.add_url_rule("/chart-data", "get_chart_data", get_chart_data)
    app.add_url_rule("/min-max-profit", "get_min_max_profit_data", get_min_max_profit_data)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
