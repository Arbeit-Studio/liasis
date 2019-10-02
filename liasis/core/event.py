from datetime import datetime
from typing import NewType, Optional
from uuid import UUID

EventId = NewType('EventId', UUID)


class EventMetaClass(type):

    def __new__(mcls, name, bases, attrs):
        return super().__new__(mcls, name, bases, attrs)

    @classmethod
    def __prepare__(mcls, name, bases, **kwargs):
        return super().__prepare__(mcls, name, bases, **kwargs)


class Event(metaclass=EventMetaClass):

    def __init__(self,
                 id: EventId,
                 occurred_on: datetime,
                 version: Optional[int] = None,
                 ):
        self.id = id
        self.occurred_on = occurred_on
        self.version = version

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'<{class_name}: {self.id}>'
