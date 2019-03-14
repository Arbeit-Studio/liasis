from typing import Any, Optional, Callable
from liasis.core.errors import Error
from liasis.core.protocols import UseCase, Presenter, Request, Response


class BaseUseCase(UseCase):

    def __init__(self, presenter: Presenter, *args, **kwargs) -> None:
        self.presenter = presenter

    def __call__(self, request: Request) -> Presenter:
        try:
            response = self.on_success(self.handle(request))
        except Exception as error:
            response = self.on_error(error)
        finally:
            return self.respond(response)
            
    def handle(self, request: Request) -> Response:
        return Response()

    def on_success(self, response: Response) -> Response:
        return response

    def on_error(self, error: Exception) -> Response:
        return Response(error=error)

    def respond(self, response: Response) -> Presenter:
        return self.presenter(response)