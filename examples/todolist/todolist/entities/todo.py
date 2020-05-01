from uuid import uuid4

from liasis import Entity, EntityId

TodoId = EntityId  # renaming variables can give your api more expresion


class Todo(Entity):

    def __init__(self, id: TodoId, description: str, done: bool) -> None:
        self.id = id
        self.description = description
        self.done = done

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.id, self.description, self.done))

    def __repr__(self):
        return f'<Todo {self.id[:7]}...>'

    def __str__(self):
        return self.description

    def do(self):
        self.done = True

    def undo(self):
        self.done = False

    def toggle(self):
        self.done = not self.done

    @classmethod
    def new(cls, description: str):
        return cls(uuid4().hex, description, False)
