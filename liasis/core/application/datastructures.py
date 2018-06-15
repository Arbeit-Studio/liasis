from dataclasses import dataclass
from liasis.core.domain import DataStructure


@dataclass
class Request(DataStructure):
    """
    Request attributes are specific for each UseCase, so te base dataclass
    doesn't define any default attributes. It's a job for the UseCase devolope
    to define how the request should look like.
    """
    pass


@dataclass
class Response(DataStructure):
    """
    Response data structure defines default attributes as a hint of how we 
    think is a good way to pass response structures to a presenter. It defines 
    a 'success: bool', 'message: str' and 'data: DataStructure' attributes, so 
    we have the minimum to handle success, failure and data that should be 
    passed to the presenter in order to create a presentation accordinly.
    """
    success: bool
    message: str
    data: DataStructure