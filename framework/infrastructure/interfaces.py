from abc import ABC, abstractmethod
from typing import Any, List, Optional

from framework.domain import Entity, EntityId


class Repository(ABC):

    @abstractmethod
    def __init__(self, session = None) -> None:
        raise NotImplementedError

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
    def filter(self, **filters) -> List[Entity]:
        raise NotImplementedError
