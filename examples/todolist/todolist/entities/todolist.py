from __future__ import annotations

from collections import defaultdict
from uuid import uuid4

from todolist.entities import Todo
from todolist.exceptions import TodoNotInList


class TodoList:
    """
    This entity doesn't inherit from liasis.Entity and that is fine.

    Much of the things on liasis are just Protocols for you to follow, they
    don't need to be explicitly implemented given protocols are considered
    structural typing.

    As long as your objects follow the structure from the protocols you are fine.
    """

    def __init__(self, id: str, name: str, todos: list[Todo] = None):
        self.id = id
        self.name = name
        self.todos = todos or []

    # --------- Public API ----------------

    @classmethod
    def new(cls, name: str):
        return cls(uuid4().hex, name)

    def new_todo(self, description: str):
        new_todo = Todo.new(description)
        self.todos.append(new_todo)

    def index(self, todo: Todo):
        try:
            return self.todos.index(todo)
        except ValueError:
            raise TodoNotInList(f'{todo} not in list')

    def remove(self, todo: Todo):
        try:
            self.todos.remove(todo)
        except ValueError:
            raise TodoNotInList(f'{todo} not in list')

    def insert(self, todo: Todo, at: int):
        self.todos.insert(at, todo)

    def move(self, todo: Todo, to: int):
        from_index = self.todos.index(todo)

