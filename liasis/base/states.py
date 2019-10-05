from liasis import State, Event
from liasis.core.errors import FinalStateError


class FinalState(State):
    """
    A Final State raises a FinalStateError if receives a Event.
    """

    def on(self, event: Event):
        raise FinalStateError(
            f"{self.__class__.__name__} is a final state but received a "
            f"unexpected {event.__class__.__name__} event.")
