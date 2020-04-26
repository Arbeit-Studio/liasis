from dataclasses import dataclass, asdict
from typing import *


@dataclass
class Data:

    @classmethod
    def of(cls, obj: object) -> 'Data':
        raise NotImplementedError

    def asdict(self):
        return asdict(self)


@dataclass
class Request(Data):
    pass


@dataclass
class Response(Data):
    data: Optional[Data] = None
    error: Optional[Exception] = None

    @classmethod
    def of(cls, obj: object) -> 'Response':
        dto = cls.__annotations__['data']
        return cls(data=dto(**obj.__dict__))
