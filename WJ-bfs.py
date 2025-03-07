# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    initial_state = (0, 0)
    visited = set()
    queue = deque([initial_state])
    parent = {initial_state: None}

    while queue:
        jug1, jug2 = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        if jug1 == target or jug2 == target:
            # Reconstruct the path
            path = []
            current_state = (jug1, jug2)
            while current_state is not None:
                path.append(current_state)
                current_state = parent[current_state]
            path.reverse()
            return path

        next_states = [
            (jug1_capacity, jug2),         # Fill jug1
            (jug1, jug2_capacity),         # Fill jug2
            (0, jug2),                     # Empty jug1
            (jug1, 0),                     # Empty jug2
            (min(jug1_capacity, jug1 + jug2), jug2 - min(jug2, jug1_capacity - jug1)),  # Pour jug2 into jug1
            (jug1 - min(jug1, jug2_capacity - jug2), min(jug2_capacity, jug1 + jug2))   # Pour jug1 into jug2
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)
                parent[state] = (jug1, jug2)

    return None

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 1

solution_path = water_jug_problem(jug1_capacity, jug2_capacity, target)
if solution_path:
    print("Solution Path:")
    for step in solution_path:
        print(step)
else:
    print("solution for same doesn't exist")
