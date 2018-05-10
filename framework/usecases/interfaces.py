from abc import ABC, abstractmethod
from typing import Any, Dict, NamedTuple, NewType, Optional

from framework.infrastructure.interfaces import Repository

Response = NamedTuple
Request = NamedTuple


class Adapter(ABC):

    @abstractmethod
    def __call__(self, data: NamedTuple):
        raise NotImplementedError


class OutputPort(ABC):

    def __init__(self, adapter: Adapter) -> None:
        self._adapter = adapter

    @abstractmethod
    def __call__(self, response: Response) -> Adapter:
        raise NotImplementedError


class InputPort(ABC):

    def __init__(self, repository: Repository, presenter: OutputPort = None) -> None:
        self._repository = repository
        self._presenter = presenter

    @abstractmethod
    def __call__(self, request: Request) -> Response:
        raise NotImplementedError
