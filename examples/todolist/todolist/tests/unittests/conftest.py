from pytest import fixture

from todolist.entities import Todo
from todolist.entities.todolist import TodoList


@fixture
def new_todo():
    return Todo.new('new todo')


@fixture
def newer_todo():
    return Todo.new('newer todo')


@fixture
def done_todo():
    todo = Todo.new('todo')
    todo.do()
    return todo


@fixture
def new_todolist():
    return TodoList.new('Reminders')


@fixture
def todolist_with_three_todos():
    tdl = TodoList.new('groceries')
    tdl.new_todo('milk')
    tdl.new_todo('bread')
    tdl.new_todo('cheese')
    return tdl
