from dataclasses import dataclass
from typing import Type, Optional
from liasis.core.entity import Entity


@dataclass
class DTO:
    pass


@dataclass
class Request(DTO):
    pass


@dataclass
class Response(DTO):
    data: Optional[DTO] = None
    error: Optional[Exception] = None
