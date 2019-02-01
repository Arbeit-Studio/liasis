from liasis.core.protocols import Adapter


class BaseAPIAdapter(Adapter):

    def __init__(self, *args, **kwargs) -> None:
        raise NotImplementedError