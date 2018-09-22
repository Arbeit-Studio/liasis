from abc import abstractmethod
from typing import List, Union, Any, Text
from liasis.core.types import Protocol, Type, EntityId, Entity
from liasis.core.datastructures import Request, Response

class Initializable(Protocol):

    @abstractmethod
    def __init__(self, *args, **kwargs):
        raise NotImplementedError


class Callable(Protocol):
    """
    Describes a callable capable of dependency injection through the __init__ method.
    """

    @abstractmethod
    def __call__(self, *args, **kwargs) -> Any:
        raise NotImplementedError


class Adapter(Initializable):
    pass


class Presenter(Callable, Initializable):


    def __init__(self, adapter: Adapter, *args, **kwargs) -> None:
        self.adapter = adapter

    def __call__(self, response: Response, *args, **kwargs) -> Union[Adapter, Text]:
        if response.error:
            return str(response.error)
        if response.data is None:
            return {}
        if isinstance(response.data, list):
            return [self.adapter(**vars(each)) for each in response.data]
        else:
            return self.adapter(response.data, *args, **kwargs)


class UseCase(Callable, Initializable):

    @abstractmethod
    def __init__(self, presenter: Presenter, *args, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def __call__(self, request: Request) -> Response:
        raise NotImplementedError


class Repository(Initializable):
    """
    Repository is a source of data, specifically the state of the application entities.
    No matter where the data come from, it could be a database or a plain file.
    """
    @abstractmethod
    def save(self, entity: Entity) -> Entity:
        raise NotImplementedError

    @abstractmethod
    def get(self, id: EntityId) -> Entity:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: EntityId) -> None:
        raise NotImplementedError

    @abstractmethod
    def search(self, **params) -> List[Entity]:
        raise NotImplementedError


class Service(Initializable):
    """
    Service gather any implementation details to 
    handle an external integration and exposes a better api to be used by
    the Usecase.
    """
    pass


class UnityOfWork(Protocol):
    """
    A context manager to encapsulate a execution scope.
    """
    @abstractmethod
    def __enter__(self):
        raise NotImplementedError

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        raise NotImplementedError


class DatabaseConnector(UnityOfWork, Initializable):
    @abstractmethod
    def connect(self, *args, **kwargs):
        raise NotImplementedError