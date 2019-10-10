from liasis import Singleton
from liasis.core import Notifier, ListenersMap


class BaseNotifier(Singleton, Notifier):
    """
    A singleton implementation of the EventDispatcher.
    """
    def __init__(self, listeners: ListenersMap = None):
        self.listeners = listeners or {}
