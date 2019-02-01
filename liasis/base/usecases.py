from typing import Any, Optional
from liasis.core.errors import Error
from liasis.core.protocols import UseCase, Presenter
from liasis.core.datastructures import Request, Response


class BaseUseCase(UseCase):

    def __init__(self, presenter: Presenter, *args, **kwargs) -> None:
        self.presenter = presenter
        self.data = None
        self.error = None

    def __call__(self, request: Request) -> Presenter:
        response = Response(None, None)
        try:
            response = self.handle(request)
        except Exception as e:
            response = self.on_error(e)
        finally:
            return self.presenter(response)

    def handle(self, request: Request) -> Response:
        raise NotImplementedError

    def on_error(self, error: Exception) -> Response:
        return Response(data=None, error=error)
