from abc import ABCMeta, abstractmethod
from typing import NewType, Optional
from uuid import UUID


class TypeMetaclass(ABCMeta):
    pass


class Type(metaclass=TypeMetaclass):
    pass


EntityId = NewType('EntityId', UUID)


class Entity(Type):

    @abstractmethod
    def __init__(self, id: Optional[EntityId], *args, **kwargs) -> None:
        raise NotImplementedError

    def __eq__(self, other):
        return vars(self) == vars(other)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'<{class_name}: {self.id}>'
