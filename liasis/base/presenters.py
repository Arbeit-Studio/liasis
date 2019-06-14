from collections import Iterable
from liasis.core import PresenterProtocol, AdapterProtocol
from liasis.core.errors import DomainError, InfrastructureError


# TODO: Handle cases like, search, pagination, and errors.
class BaseHttpPresenter(PresenterProtocol):

    def __init__(self, adapter: AdapterProtocol, *args, **kwargs) -> None:
        self.adapter = adapter

    def __call__(self, response, *args, **kwargs):
        if isinstance(response, DomainError):
            return self.on_domain_error(response)
        if isinstance(response, InfrastructureError):
            return self.on_infrastructure_error(response)
        if isinstance(response, Exception):
            return self.on_unknown_error(response)
        return self.on_success(response)

    def on_success(self, response):
        collection = isinstance(response, Iterable)
        return self.adapter(response, collection), 200

    def on_domain_error(self, response):
        return self.adapter(response), 409

    def on_infrastructure_error(self, response):
        return self.adapter(response), 500

    def on_unknown_error(self, response):
        return self.adapter(response), 500
