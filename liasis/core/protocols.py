from typing import List, Any, Iterable

from typing_extensions import Protocol

from liasis.core.types import EntityId, Entity
from liasis.core.datastructures import Request, Response


class Adapter(Protocol):

    def __call__(self, response, *args, **kwargs): ...


class Presenter(Protocol):

    def __init__(self, adapter: Adapter, *args, **kwargs) -> None: ...

    def __call__(self, response: Response, *args, **kwargs) -> Any: ...


class UseCase(Protocol):

    def __init__(self, presenter: Presenter, *args, **kwargs) -> None: ...

    def __call__(self, request: Request) -> Presenter: ...


class Repository(Protocol):
    """
    A Repository is responsible for storing and retrieving entities.
    No matter where the data come from, it could be a database or a plain file.
    """
    def save(self, entity: Entity) -> Entity: ...

    def get(self, id: EntityId) -> Entity: ...

    def delete(self, id: EntityId) -> None: ...

    def search(self, **kwargs) -> List[Entity]: ...


class Service(Protocol):
    """
    Services, different from repositories, do not handle storing and retrieval
    of entities state. It's more suitable for things like, e-mails sending.
    """


class Gateway(Protocol):
    """
    Gateways are responsible for integrating with external sources and abstract
    implementation details from inner components like Repositories and Services.
    Examples of Gateways are, REST and SOAP API clients.
    """