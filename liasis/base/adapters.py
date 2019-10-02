from liasis.core.protocols import AdapterProtocol
import json


class BaseAPIAdapter(AdapterProtocol):

    def __call__(self, response, *args, **kwargs) -> str:
        if response.errors:
            return json.dumps(response.errors.__dict__)
        return json.dumps(response)