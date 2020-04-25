from dataclasses import dataclass, asdict


@dataclass
class DTO:

    @classmethod
    def of(cls, obj: object) -> 'DTO':
        return cls(**obj.__dict__)

    def asdict(self):
        return asdict(self)


@dataclass
class Request(DTO):
    pass


@dataclass
class Response(DTO):
    data: DTO = None
    error: Exception = None

    @classmethod
    def of(cls, obj: object) -> 'Response':
        dto = cls.__annotations__['data']
        return cls(data=dto(**obj.__dict__))
