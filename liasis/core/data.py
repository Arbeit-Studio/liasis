from collections import UserDict
from typing import Type
import json
from liasis.core.entity import Entity


class DTO(dict):
    __entity = User
    
    def __getattr__(self, name):
        return self.get(name)

    def entity(self):
        if self.__entity:
            return self.__entity(**self)
        else:
            raise AttributeError('This DTO does not represents an Entity.')


class Request(DTO): ...


class Response(DTO):

    def __init__(self, *args, error: Exception = None, **kwargs):
        self.errors = error
        super().__init__(*args, **kwargs)

    def __bool__(self):
        if self.errors:
            return False
        return True


class EntityData(EntityDataProtocol):

    __entity__: Type[Entity] = None

    def __init__(self) -> None:
        if self.__entity__:
            pass

    def __eq__(self, other: 'EntityData') -> bool: ...

    def __repr__(self) -> str: ...    
