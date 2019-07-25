from liasis.core.protocols import AdapterProtocol
from liasis.core.errors.infrastructure import InfrastructureError
from liasis.core.protocols import ResponseProtocol
import json


class BaseAPIAdapter(AdapterProtocol):

    def __call__(self, response, *args, **kwargs) -> str:

        if not isinstance(response, ResponseProtocol):
            raise InfrastructureError(code=1, title='Adapter Error', message='Error on passing Response to Adapter '+__name__)

        if response.error:
            return json.dumps(response.error.__dict__)
        return json.dumps(response.data)