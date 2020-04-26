from todolist.entities import Todo


def test_id_is_created_for_new_todo():
    todo = Todo.new('study')
    assert todo.id is not None


def test_todo_is_not_done_when_created():
    todo = Todo.new('work')
    assert todo.done is False


def test_doing_a_todo(new_todo):
    new_todo.do()
    assert new_todo.done is True


def test_undoing_a_todo(done_todo):
    done_todo.undo()
    assert done_todo.done is False


def test_tooling_a_todo(new_todo):
    new_todo.toggle()
    assert new_todo.done is True
    new_todo.toggle()
    assert new_todo.done is False


def test_for_todo_equality(new_todo):
    other_todo = Todo(**new_todo.__dict__)
    assert new_todo == other_todo
    other_todo.done = not new_todo.done
    assert new_todo != other_todo
