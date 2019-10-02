from liasis.core import EventDispatcher, Singleton, ListenersDict


class BaseEventDispatcher(EventDispatcher, metaclass=Singleton):
    """
    A singleton implementation of the EventDispatcher.
    """
    def __init__(self, listeners: ListenersDict = None):
        self.listeners = listeners or {}
