class Error(Exception):
    """
    Base error Exception which all other exceptions derive from.
    """


class DomainError(Error):
    """
    Domain Error is used to indicate an error in the domain layer.
    """


class BusinessRuleError(DomainError):
    """
    A Generic exception to indicate a bussines rule not meet.
    """


class InvalidEventEntityError(DomainError):
    """
    Raised when
    """


class FinalStateError(DomainError):
    """
    Raised when a final state receives an Event.
    """


class InvalidEventError(DomainError):
    """
    Raised when a state receives a invalid Event.
    """


class InvalidEventVersionError(DomainError):
    """
    Raised when a event receives a Event with invalid version.
    """


class InfrastructureError(Error):
    """
    An Error on infrastructure layer.
    """


class IOError(InfrastructureError):
    """
    Generic IO error.
    """


class NetworkError(IOError):
    """
    An specific IO error when dealing with networking.
    """


class ConfigError(InfrastructureError):
    """Base class for exceptions related to configuration"""