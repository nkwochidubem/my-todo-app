FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the
    list of todo items

    :param filepath:
    :return: None
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    """
    Write the todos items list in the text file

    :param todos:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos)


if __name__ == "__main__":
    print("hello from functions")
