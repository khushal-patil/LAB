import heapq
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def manhattan_distance(state, goal_state):
    distance = 0
    for r in range(3):
        for c in range(3):
            value = state[r][c]
            if value != 0:  
                goal_r, goal_c = divmod(value - 1, 3)
                distance += abs(goal_r - r) + abs(goal_c - c)
    return distance

def is_goal_state(state, goal_state):
    return state == goal_state

def get_neighbors(state):
    neighbors = []
    # Find the blank space (0)
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                blank_pos = (r, c)
                break

    for dr, dc in directions:
        new_r, new_c = blank_pos[0] + dr, blank_pos[1] + dc
        if 0 <= new_r < 3 and 0 <= new_c < 3:  
            new_state = [row[:] for row in state]
            new_state[blank_pos[0]][blank_pos[1]], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[blank_pos[0]][blank_pos[1]]
            neighbors.append(new_state)
    return neighbors

def a_star(start_state, goal_state):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start_state, goal_state), 0, start_state, []))  
    visited = set()

    while open_list:
        f, g, current_state, path = heapq.heappop(open_list)

        if is_goal_state(current_state, goal_state):
            return path + [current_state]

        visited.add(tuple(map(tuple, current_state)))  
        neighbors = get_neighbors(current_state)

        for neighbor in neighbors:
            if tuple(map(tuple, neighbor)) not in visited:
                h = manhattan_distance(neighbor, goal_state)
                heapq.heappush(open_list, (g + 1 + h, g + 1, neighbor, path + [current_state]))

    return None  # If no solution is found

def get_input_matrix():
    matrix = []
    print("Enter the 3x3 puzzle (enter 0 for the blank space):")
    for i in range(3):
        row = list(map(int, input(f"Enter row {i+1} (3 space-separated numbers): ").split()))
        if len(row) != 3:
            print("Each row must contain exactly 3 numbers. Please try again.")
            return get_input_matrix()
        matrix.append(row)
    return matrix

print("Welcome to the 8-Puzzle Solver!")
start_state = get_input_matrix()
print("Enter the goal state matrix:")
goal_state = get_input_matrix()

solution = a_star(start_state, goal_state)
    
if solution:
    print(f"Solution path found in {len(solution) - 1} steps:")
    for step in solution:
        for row in step:
            print(row)
        print()
        # Print the Manhattan distance for each step
        distance = manhattan_distance(step, goal_state)
        print(f"Manhattan distance to goal: {distance}\n")
else:
    print("No solution found.")

