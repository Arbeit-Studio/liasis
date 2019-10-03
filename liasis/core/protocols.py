from abc import abstractmethod
from typing import List, Any, Dict, Type, Set
from typing_extensions import Protocol

from liasis.core.data import Response, Request
from liasis.core.entity import EntityId, Entity

from liasis.core.event import Event


class AdapterProtocol(Protocol):

    def __call__(self, response, *args, **kwargs): ...


class PresenterProtocol(Protocol):

    def __init__(self, adapter: AdapterProtocol, *args, **kwargs) -> None: ...

    def __call__(self, response: Response, *args, **kwargs) -> Any: ...


class UseCaseProtocol(Protocol):

    def __init__(self, presenter: PresenterProtocol, *args, **kwargs) -> None: ...

    def __call__(self, request: Request) -> PresenterProtocol: ...


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


class ListenerProtocol(Protocol):
    """
    Any object which need to listen to a event must implement the EventListener
    protocol.
    """

    @abstractmethod
    def notify(self, event: Event):
        raise NotImplementedError


ListenersMap = Dict[Type[Event], Set[ListenerProtocol]]


class NotifierProtocol(Protocol):
    """
    Manages events subscription and dispatching for different types of events.
    """
    listeners: ListenersMap

    def subscribe(self, event: Type[Event], listener: ListenerProtocol):
        self.listeners.setdefault(event, set()).add(listener)

    def unsubscribe(self, event: Type[Event], listener: ListenerProtocol):
        self.listeners.setdefault(event, set()).discard(listener)

    def notify(self, event: Event):
        for listener in self.listeners.get(event.__class__):
            listener.notify(event)
