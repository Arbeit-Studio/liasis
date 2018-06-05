from dataclasses import dataclass
from abc import ABC, abstractmethod, ABCMeta
from typing import Any, Dict, NamedTuple, NewType, Optional

from liasis.infrastructure import Repository


class Base(mata=ABCMeta):
    pass


@dataclass
class Request:
    pass


@dataclass
class Response:
    pass


class Adapter(ABC):

    @abstractmethod
    def __call__(self, data: NamedTuple):
        raise NotImplementedError


class Presenter(ABC):

    def __init__(self, adapter: Adapter) -> None:
        self._adapter = adapter

    @abstractmethod
    def __call__(self, response: Response) -> Adapter:
        raise NotImplementedError


class UseCase(ABC):

    def __init__(self, *args, **kwargs) -> None:
        self._repository = repository
        self._presenter = presenter

    @abstractmethod
    def __call__(self, request: Request) -> Response:
        raise NotImplementedError
