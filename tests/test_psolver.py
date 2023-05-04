import os

import pytest

from psolver import read_states

csv_states = []
csv_states_expected = []

read_states_config = [
    ("npuzzle",
     [
         "0,1,2,3,4,5,6,7,8",
         "5,4,3,2,1,0,6,8,7",
         "1,0,2,8,4,7,5,6,3",
     ],
     [
         (0, 1, 2, 3, 4, 5, 6, 7, 8),
         (5, 4, 3, 2, 1, 0, 6, 8, 7),
         (1, 0, 2, 8, 4, 7, 5, 6, 3),
     ],
     ),
    ("romania",
     [
         "Arad,Bucharest",
         "Sibiu,Urziceni",
         "Timisoara,Lugoj",
         "Vaslui,Eforie",
     ],
     [
         ("Arad", "Bucharest"),
         ("Sibiu", "Urziceni"),
         ("Timisoara", "Lugoj"),
         ("Vaslui", "Eforie"),
     ],
     )
]


@pytest.mark.parametrize("problem, csv_states, expected_states", read_states_config)
def test_read_states(problem, csv_states, expected_states):
    # Create a temporary file with initial states
    i = 0
    file_name = f"test({i})"
    while os.path.exists(file_name):
        i += 1
        file_name = f"test({i})"

    with open(file_name, "w") as file:
        for csv_state in csv_states:
            file.write(csv_state + "\n")

    states = read_states(file_name, problem)
    os.remove(file_name)

    assert states == expected_states
