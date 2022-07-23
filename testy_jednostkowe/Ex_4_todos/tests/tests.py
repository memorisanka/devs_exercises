from functionality.src import *


def test_check_if_adds_todo():
    if len(todos) == 0:
        assert Exception
    else:
        content = "Make laundry"
        add_todo(content)
        result = todos[len(todos)-1]

        assert result == content


def test_check_if_removes_todo():
    pos = 1
    if len(todos) == 0 or pos >= len(todos) or pos < 0:
        assert Exception
    else:
        start = len(todos)
        remove_todo(pos)
        result = start - 1
        assert len(todos) == result


def test_check_if_edits_todo():
    pos = 1
    if len(todos) == 0 or pos >= len(todos) or pos < 0:
        assert Exception
    else:
        content = "Make dinner"
        edit_todo(pos, content)
        assert todos[pos] == content


def test_check_if_removes_all():
    todos.clear()
    assert todos == []  # or len(todos) == 0
    