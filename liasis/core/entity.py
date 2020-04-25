from typing import *
from uuid import UUID


EntityId = NewType('EntityId', UUID)


class EntityMetaClass(type):

    def __new__(mcls, name, bases, attrs):
        return super().__new__(mcls, name, bases, attrs)

    @classmethod
    def __prepare__(mcls, name, bases, **kwargs):
        return super().__prepare__(mcls, name, bases, **kwargs)


class Entity(metaclass=EntityMetaClass):

    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return vars(self) == vars(other)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'<{class_name}: {self.id}>'
