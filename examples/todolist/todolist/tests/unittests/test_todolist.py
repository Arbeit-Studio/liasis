from todolist.entities.todolist import TodoList

from todolist.entities import Todo


def test_todolist_is_created_correctly():
    todolist = TodoList.new(name='groceries')
    assert todolist.id is not None
    assert todolist.name == 'groceries'
    assert not todolist.todos


def test_create_a_new_todo(new_todolist):
    assert not new_todolist.todos
    new_todolist.new_todo('walk the dog')
    assert len(new_todolist.todos) == 1


def test_todolist_index(todolist_with_three_todos):
    tdl = todolist_with_three_todos
    expected_index = 1
    td = tdl.todos[expected_index]
    td_index = tdl.index(td)
    assert td_index == expected_index


def test_remove_todo_from_list(todolist_with_three_todos):
    tdl = todolist_with_three_todos
    td = tdl.todos[0]
    tdl.remove(td)
    assert td not in tdl.todos


def test_insert_todo_in_list(todolist_with_three_todos):
    tdl = todolist_with_three_todos
    todo = Todo.new('do some stuff')
    tdl.insert(todo, 0)
    assert tdl.todos[0] is todo


# def test_move_todo_in_list(todolist_with_three_todos):
#     tdl = todolist_with_three_todos
#     td = tdl.todos[0]  # Avoid access todos directly, this is just for the test
#     tdl.move(td, 2)
#     assert tdl.todos.index(td) == 2
