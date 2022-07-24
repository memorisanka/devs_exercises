todos = ["Clean my room", "Make my bed", "Go to school", "Do school homework"]


def check_pos(pos: int) -> None:
    if len(todos) == 0:
        raise Exception("No more todos!")
    elif pos >= len(todos) or pos < 0:
        raise Exception("No such item number!")


def add_todo(todo: str) -> None:
    todos.append(todo)


def remove_todo(pos: int) -> None:
    check_pos(pos)

    todos.pop(pos)


def edit_todo(pos: int, todo: str) -> None:
    check_pos(pos)

    todos[pos] = todo


def remove_all():
    todos.clear()


add_todo("Go to bed")
remove_todo(0)
edit_todo(0, "Get up from bed")
remove_all()
