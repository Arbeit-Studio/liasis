class Error(Exception):
    
    def __init__(self, code: int, title: str, message: str) -> None:
        self.code = code
        self.title = title
        self.message = message
    
    def __str__(self):
        return f"{self.title}: {self.message} Código:{self.code}"


from .domain import *
from .infrastructure import *