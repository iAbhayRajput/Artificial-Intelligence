# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def water_jug_problem_dfs(jug1_capacity, jug2_capacity, target):
    initial_state = (0, 0)
    visited = set()
    stack = [initial_state]
    parent = {initial_state: None}

    while stack:
        jug1, jug2 = stack.pop()  # Pop the top state from the stack

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
            (jug1_capacity, jug2),         # Fill Jug 1
            (jug1, jug2_capacity),         # Fill Jug 2
            (0, jug2),                     # Empty Jug 1
            (jug1, 0),                     # Empty Jug 2
            (min(jug1_capacity, jug1 + jug2), jug2 - min(jug2, jug1_capacity - jug1)),  # Pour Jug 2 into Jug 1
            (jug1 - min(jug1, jug2_capacity - jug2), min(jug2_capacity, jug1 + jug2))   # Pour Jug 1 into Jug 2
        ]

        for state in next_states:
            if state not in visited:
                stack.append(state)
                parent[state] = (jug1, jug2)

    return None

# Example usage
jug1_capacity = 5
jug2_capacity = 4
target = 3

solution_path = water_jug_problem_dfs(jug1_capacity, jug2_capacity, target)
if solution_path:
    print("Solution Path:")
    for step in solution_path:
        print(step)
else:
    print("No solution found.")
