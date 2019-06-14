from typing import List, Any, Iterable, Mapping
from typing_extensions import Protocol
from liasis.core.types import EntityId, Entity
from collections import UserDict


class RequestProtocol(Protocol):

    data: dict


class ResponseProtocol(Protocol):

    data: dict
    error: Exception = None

    def __bool__(self): ...


class AdapterProtocol(Protocol):

    def __call__(self, response, *args, **kwargs): ...


class PresenterProtocol(Protocol):

    def __init__(self, adapter: AdapterProtocol, *args, **kwargs) -> None: ...

    def __call__(self, response: ResponseProtocol, *args, **kwargs) -> Any: ...


class UseCaseProtocol(Protocol):

    def __init__(self, presenter: PresenterProtocol, *args, **kwargs) -> None: ...

    def __call__(self, request: RequestProtocol) -> PresenterProtocol: ...


class RepositoryProtocol(Protocol):
    """
    A Repository is responsible for storing and retrieving entities.
    No matter where the data come from, it could be a database or a plain file.
    """
    def save(self, entity: Entity) -> Entity: ...

    def get(self, id: EntityId) -> Entity: ...

    def delete(self, id: EntityId) -> None: ...

    def search(self, **kwargs) -> List[Entity]: ...


class ServiceProtocol(Protocol):
    """
    Services, different from repositories, do not handle storing and retrieval
    of entities state. It's more suitable for things like, e-mails sending.
    """


class GatewayProtocol(Protocol):
    """
    Gateways are responsible for integrating with external sources and abstract
    implementation details from inner components like Repositories and Services.
    Examples of Gateways are, REST and SOAP API clients.
    """

