from liasis import Singleton
from liasis.core import NotifierProtocol, ListenersMap


class BaseNotifier(Singleton, NotifierProtocol):
    """
    A singleton implementation of the EventDispatcher.
    """
    def __init__(self, listeners: ListenersMap = None):
        self.listeners = listeners or {}
