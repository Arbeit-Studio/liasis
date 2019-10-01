from liasis.core.errors import Error


class DomainError(Error):
    """
    Domain Error is used to indicate an error in the domain layer.
    """

class BussinessRuleError(DomainError):
    """
    A Generic exception to indicate a bussines rule not meet.
    """
