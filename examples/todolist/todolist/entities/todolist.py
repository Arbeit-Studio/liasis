from __future__ import annotations

from collections import defaultdict
from uuid import uuid4

from todolist.entities import Todo, TodoId
from todolist.exceptions import TodoNotInList

from examples.todolist.todolist.exceptions import TodoAlreadyInList

TodoListId = [str, int]


class TodoList:
    """
    This entity doesn't inherit from liasis.Entity and that is fine.

    Much of the things on liasis are just Protocols for you to follow, they
    don't need to be explicitly implemented given protocols are considered
    structural typing.

    As long as your objects follow the structure from the protocols you are fine.
    """

    def __init__(self, id: TodoListId, name: str, todos: list[Todo] = None):
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
            raise TodoNotInList(f'{todo} not in list') from None

    def remove(self, todo: Todo):
        try:
            self.todos.remove(todo)
        except ValueError:
            raise TodoNotInList(f'{todo} not in list') from None

    def insert(self, todo: Todo, at: Optional[int] = None):
        if todo not in self.todos:
            index = at if at is not None else len(self.todos)
            self.todos.insert(index, todo)
        else:
            raise TodoAlreadyInList(f'{todo} is already in the list. Try to move it')

    def move(self, todo: Todo, to: int):
        try:
            from_ = self.todos.index(todo)
            self.todos.insert(to, self.todos.pop(from_))
        except (ValueError, IndexError):
            raise TodoNotInList(f'{todo} not in list') from None

    def get(self, id: TodoId):
        try:
            return next(filter(lambda x: x.id == id,  self.todos))
        except StopIteration:
            raise TodoNotInList from None
