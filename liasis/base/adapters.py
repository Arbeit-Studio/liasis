from liasis.core.protocols import Adapter
import json


class BaseAPIAdapter(Adapter):

    def __call__(self, response, *args, **kwargs) -> str:
        if response.errors:
            return json.dumps(response.errors.__dict__)
        return json.dumps(response)