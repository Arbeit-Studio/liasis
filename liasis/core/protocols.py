from abc import abstractmethod
from functools import reduce
from typing import List, Any, Dict, Type, Set, ClassVar, TypeVar, Union, Optional, Iterable
from typing_extensions import Protocol

from liasis.core.errors import InvalidEventError, InvalidEventVersionError, InvalidEventEntityError, NotHandledError
from liasis.core.data import Response, Request
from liasis.core.entity import EntityId, Entity

from liasis.core.event import Event


class Adapter(Protocol):
    following: Optional['Adapter']

    @abstractmethod
    def can_handle(self, response: Response) -> bool:
        raise NotImplementedError

    @abstractmethod
    def handle(self, response: Response) -> Any:
        raise NotImplementedError

    def __call__(self, response: Response) -> Any:
        if self.can_handle(response):
            return self.handle(response)
        if self.following:
            return self.following(response)
        raise NotHandledError('The response was not handled by any adapter.', response)


class Presenter:
    adapters = Iterable[Type[Adapter]]

    def __init__(self):
        self.chain = reduce(lambda f, n: n(f), self.adapters[::-1], None)

    def __call__(self, response: Response) -> Any:
        try:
            return self.chain(response)
        except NotHandledError:
            raise


class UseCase(Protocol):
    presenter: Presenter

    def __call__(self, request: Request) -> Presenter:
        try:
            response = self.on_success(self.handle(request))
        except Exception as error:
            response = self.on_error(error)
        finally:
            return self.respond(response)

    @abstractmethod
    def handle(self, request: Request) -> Response:
        raise NotImplementedError

    def on_success(self, response: Response) -> Response:
        return response

    def on_error(self, error: Exception) -> Response:
        return Response(error=error)

    def respond(self, response: Response) -> Presenter:
        return self.presenter(response)


E = TypeVar('E')


class Repository(Protocol[E]):
    """
    A Repository is responsible for storing and retrieving entities.
    No matter where the data come from, it could be a database or a plain file.
    """

    @abstractmethod
    def save(self, entity: E) -> E: ...

    @abstractmethod
    def get(self, id: EntityId) -> E: ...

    @abstractmethod
    def delete(self, id: EntityId) -> None: ...

    @abstractmethod
    def search(self, **kwargs) -> Union[E, List[E]]: ...


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


class Listener(Protocol):
    """
    Any object which need to listen to a event must implement the EventListener
    protocol.
    """

    @abstractmethod
    def notify(self, event: Event):
        raise NotImplementedError


ListenersMap = Dict[Type[Event], Set[Listener]]


class Notifier(Protocol):
    """
    Manages events subscription and dispatching for different types of events.
    """
    listeners: ListenersMap

    def subscribe(self, event: Type[Event], listener: Listener):
        self.listeners.setdefault(event, set()).add(listener)

    def unsubscribe(self, event: Type[Event], listener: Listener):
        self.listeners.setdefault(event, set()).discard(listener)

    def notify(self, event: Event):
        for listener in self.listeners.setdefault(event.__class__, set()):
            listener.notify(event)


class State(Protocol):
    """
    Represents a state of an object, also handle state transition when receives
    a event.
    """
    entity: Entity
    events: ClassVar[List[Event]]

    def on(self, event: Event):
        """
        The public API for the event, it receives an event to be handled.
        :param event: Event
        """
        self.validate_event(event)
        self.validate_version(event)
        self.validate_entity(event)
        return self.handle(event)

    @abstractmethod
    def handle(self, event: Event) -> Entity:
        """
        The handle method should be implemented by each State subclass, so it
        can handle it's events list.
        :param event: Event
        :return:
        """
        raise NotImplementedError

    def validate_event(self, event: Event):
        """
        Check if the State can handle the incoming event.
        :param event: Event
        """
        if event.__class__ not in self.events:
            raise InvalidEventError(
                f"{self.__class__.__name__} received a invalid event "
                f"{event.__class__.__name__}.")

    def validate_version(self, event: Event):
        """
        Check if the incoming event has the right version.
        :param event:
        """
        if event.version is not self.entity.version + 1:
            raise InvalidEventVersionError(
                f"{self.entity.__class__.__name__}(v{self.entity.version}) received a "
                f"invalid event {event.__class__.__name__}(v{event.version})")

    def validate_entity(self, event: Event):
        """
        Validate if the Entity from the incoming Event is the same of State.
        :param event:
        """
        if event.entity_id != self.entity.id:
            raise InvalidEventEntityError(
                f"{self.entity.__class__.__name__}(entity:{self.entity.id}) received a "
                f"invalid event {event.__class__.__name__}(entity:{event.entity_id})")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__
