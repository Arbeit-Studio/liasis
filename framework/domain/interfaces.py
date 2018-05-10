from abc import ABC, abstractmethod
from typing import Optional
from framework.domain import EntityId


class Entity(ABC):

    #### Magic Methods ####

    @abstractmethod
    def __init__(self, id: Optional[EntityId], *args, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'<{class_name}: {self.id}>'
