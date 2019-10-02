from collections import UserDict
from typing import Type, Optional
import json
from liasis.core.entity import Entity


class DTO(dict):
    __entity: Optional[Type[Entity]] = None

    def __getattr__(self, name):
        return self.get(name)

    def entity(self):
        if self.__entity:
            return self.__entity(**self)
        else:
            raise AttributeError('This DTO does not represents an Entity.')


class Request(DTO):
    pass


class Response(DTO):

    def __init__(self, *args, error: Exception = None, **kwargs):
        self.errors = error
        super().__init__(*args, **kwargs)

    def __bool__(self):
        if self.errors:
            return False
        return True
