# 8-Puzzle using Depth First Search (DFS)

def display(state):

    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])

    print()


def get_neighbors(state):

    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    # Move Up
    if row > 0:

        new_state = list(state)

        new_state[blank], new_state[blank - 3] = \
            new_state[blank - 3], new_state[blank]

        neighbors.append(tuple(new_state))

    # Move Down
    if row < 2:

        new_state = list(state)

        new_state[blank], new_state[blank + 3] = \
            new_state[blank + 3], new_state[blank]

        neighbors.append(tuple(new_state))

    # Move Left
    if col > 0:

        new_state = list(state)

        new_state[blank], new_state[blank - 1] = \
            new_state[blank - 1], new_state[blank]

        neighbors.append(tuple(new_state))

    # Move Right
    if col < 2:

        new_state = list(state)

        new_state[blank], new_state[blank + 1] = \
            new_state[blank + 1], new_state[blank]

        neighbors.append(tuple(new_state))

    return neighbors


def dfs(start, goal):

    stack = [(start, [start])]
    visited = set()

    while stack:

        state, path = stack.pop()

        # Check goal
        if state == goal:
            return path

        # Skip already visited states
        if state in visited:
            continue

        visited.add(state)

        # Generate next states
        for next_state in get_neighbors(state):

            if next_state not in visited:

                new_path = path + [next_state]

                stack.append((next_state, new_path))

    return None


# Main Program

start = tuple(map(int, input(
    "Enter initial state: "
).split()))

goal = tuple(map(int, input(
    "Enter goal state: "
).split()))

print("\nInitial State:")
display(start)

print("Goal State:")
display(goal)

solution = dfs(start, goal)

if solution:

    print("Solution Found!")
    print("Number of moves:", len(solution) - 1)

    print("\nSolution Path:")

    for i, state in enumerate(solution):

        print("Step", i)
        display(state)

else:

    print("Solution Not Found!")
