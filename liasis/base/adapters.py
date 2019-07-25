from liasis.core.protocols import AdapterProtocol
import json


class BaseAPIAdapter(AdapterProtocol):

    def __call__(self, response, *args, **kwargs) -> str:
        if response.error:
            return json.dumps(response.error.__dict__)
        return json.dumps(response.data)