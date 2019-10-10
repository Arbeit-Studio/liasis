from typing import Any, Optional, Callable
from liasis.core.errors import Error
from liasis.core.protocols import UseCase, Presenter, RequestProtocol, ResponseProtocol


class BaseUseCase(UseCase):

    def __init__(self, presenter: Presenter, *args, **kwargs) -> None:
        self.presenter = presenter

    def __call__(self, request: RequestProtocol) -> Presenter:
        try:
            response = self.on_success(self.handle(request))
        except Exception as error:
            response = self.on_error(error)
        finally:
            return self.respond(response)
            
    def handle(self, request: RequestProtocol) -> ResponseProtocol:
        return ResponseProtocol()

    def on_success(self, response: ResponseProtocol) -> ResponseProtocol:
        return response

    def on_error(self, error: Exception) -> ResponseProtocol:
        return ResponseProtocol(error=error)

    def respond(self, response: ResponseProtocol) -> Presenter:
        return self.presenter(response)