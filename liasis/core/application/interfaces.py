from dataclasses import dataclass
from abc import ABC, abstractmethod, ABCMeta
from typing import Union

from liasis.core.domain import DataStructure
from liasis.core.application import Request, Response
from liasis.core.infrastructure import Repository


class Adapter(ABC):

    @abstractmethod
    def __call__(self, data: DataStructure):
        raise NotImplementedError


class Presenter(ABC):

    def __init__(self, adapter: Adapter) -> None:
        self._adapter = adapter

    @abstractmethod
    def __call__(self, response: Response) -> Adapter:
        raise NotImplementedError


class UseCase(ABC):

    def __init__(self, repository: Repository, presenter: Presenter = None) -> None:
        self._repository = repository
        self._presenter = presenter

    @abstractmethod
    def __call__(self, request: Request) -> Response:
        raise NotImplementedError
