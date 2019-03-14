from typing import Optional
from dataclasses import dataclass


@dataclass
class DataStructure:
    """
    Base dataclass to be used as representation of Entities or any data
    crossing the domain boundary.
    """
    pass


@dataclass
class Request(DataStructure):
    """
    Request attributes are specific for each UseCase, so te base dataclass
    doesn't define any default attributes. It's a job for the UseCase developer
    to define how the request should look like.
    """
    pass


@dataclass
class Response(DataStructure):
    """
    Response data structure defines default attributes as a hint of how we 
    think is a good way to pass response structures to a presenter. It defines 
    success and error attributes, so we have the minimum to handle success or
    failure and data that should be passed to the presenter in order to create
    a presentation accordinly.
    """
    success: Optional[DataStructure] = None
    failure: Optional[Exception] = None
