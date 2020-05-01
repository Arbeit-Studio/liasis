from liasis import DomainError


class TodoNotInList(DomainError):
    pass


class TodoAlreadyInList(DomainError):
    pass
