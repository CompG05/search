import os

from psolver import read_states


def test_read_states():
    # Create a temporary file with initial states
    i = 0
    file_name = f"test({i})"
    while os.path.exists(file_name):
        i += 1
        file_name = f"test({i})"

    csv_states = [
        "0,1,2,3,4,5,6,7,8",
        "5,4,3,2,1,0,6,8,7",
        "1,0,2,8,4,7,5,6,3",
    ]

    with open(file_name, "w") as file:
        for csv_state in csv_states:
            file.write(csv_state + "\n")

    states = read_states(file_name, "NPuzzle")
    os.remove(file_name)

    assert states == [
        (0, 1, 2, 3, 4, 5, 6, 7, 8),
        (5, 4, 3, 2, 1, 0, 6, 8, 7),
        (1, 0, 2, 8, 4, 7, 5, 6, 3),
    ]
