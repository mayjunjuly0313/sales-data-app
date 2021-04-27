from dependency_injector import containers, providers

from sales_data.application.service import SalesDataApplicationService
from sales_data.infra_structure.in_memory_repository import InMemorySalesDataRepository


class Container(containers.DeclarativeContainer):
    sales_data_repository = providers.Singleton(InMemorySalesDataRepository)

    sales_data_application_service = providers.Singleton(
        SalesDataApplicationService, sales_data_repository=sales_data_repository
    )
