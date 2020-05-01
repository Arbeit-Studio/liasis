from uuid import uuid4

import pytest
from todolist.entities.todolist import TodoList

from todolist.entities import Todo

from todolist.exceptions import TodoNotInList

from examples.todolist.todolist.exceptions import TodoAlreadyInList


def test_create_todolist():
    todolist = TodoList.new(name='groceries')
    assert todolist.id is not None
    assert todolist.name == 'groceries'
    assert not todolist.todos


def test_create_a_new_todo(new_todolist):
    assert not new_todolist.todos
    new_todolist.new_todo('walk the dog')
    assert len(new_todolist.todos) == 1


def test_todolist_index(todolist_with_three_todos, new_todo):
    todolist = todolist_with_three_todos
    not_in_todolist = new_todo
    expected_index = 1
    td = todolist.todos[expected_index]
    td_index = todolist.index(td)
    assert td_index == expected_index
    with pytest.raises(TodoNotInList):
        todolist.index(not_in_todolist)


def test_remove_todo_from_list(todolist_with_three_todos):
    tdl = todolist_with_three_todos
    td = tdl.todos[0]
    tdl.remove(td)
    assert td not in tdl.todos
    with pytest.raises(TodoNotInList):
        tdl.remove(td)


def test_insert_todo_in_list(todolist_with_three_todos, new_todo, newer_todo):
    tdl = todolist_with_three_todos
    tdl.insert(new_todo, 0)
    assert tdl.todos[0] is new_todo
    tdl.insert(newer_todo)
    assert tdl.todos[-1] is newer_todo
    with pytest.raises(TodoAlreadyInList):
        tdl.insert(new_todo, 0)


def test_move_todo_in_list(todolist_with_three_todos, new_todo):
    tdl = todolist_with_three_todos
    not_in_tdl = new_todo
    todo = tdl.todos[0]
    tdl.move(todo, 2)
    assert tdl.todos.index(todo) == 2
    with pytest.raises(TodoNotInList):
        tdl.move(not_in_tdl, 0)


def test_get_todo_from_list(todolist_with_three_todos):
    # ---- setup -----
    tdl = todolist_with_three_todos
    td = tdl.todos[0]  # Avoid access todos directly, this is just for the test
    id = td.id
    # ---- actual test -----
    todo = tdl.get(id)
    assert todo == td
    with pytest.raises(TodoNotInList):
        madeup_id = uuid4().hex
        tdl.get(madeup_id)
