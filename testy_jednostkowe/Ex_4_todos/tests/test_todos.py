from functionality.src import *
import pytest

def create_test_todos():
    laundry = "Make laundry"
    bed = "Make bed"
    dinner = "Make dinner"
    add_todo(laundry)
    add_todo(dinner)
    add_todo(bed)

def test_if_check_pos_throws_no_such_item_number_exception():
    with pytest.raises(Exception) as ex1:
        create_test_todos()
        check_pos(20)
    assert "No such item number!" in str(ex1.value)


def test_if_check_pos_throws_no_more_todos_exception():
    with pytest.raises(Exception) as ex2:
        remove_all()
        check_pos(1)
    assert "No more todos!" in str(ex2.value)


def test_check_if_adds_todo():
    todo = "Make laundry"
    add_todo(todo)
    expected = todos[len(todos) - 1]

    assert expected == todo


# @classmethod
# def setup_class(cls):
#     print('\n===Setup Class===')
#
#
# @classmethod
# def teardown_class(cls):
#     print('\n===Teardown Class===')

def test_check_if_removes_todo():
    # todos jest puste
    create_test_todos()
    length_before = len(todos)

    pos = 1
    remove_todo(pos)
    length_after = len(todos)

    assert length_after == length_before - 1


def test_check_if_edits_todo():
    create_test_todos()
    pos = 1
    todo = "Make dinner"
    edit_todo(pos, todo)

    assert todos[pos] == todo


def test_check_if_removes_all():
    todos.clear()
    assert todos == []  # or len(todos) == 0
