from liasis.core.protocols import Adapter
import json


class BaseAPIAdapter(Adapter):

    def __call__(self, response, *args, **kwargs) -> str:
        if response.error:
            return json.dumps(response.error.__dict__)
        return json.dumps(response)