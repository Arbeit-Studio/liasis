from liasis.core.errors import Error


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