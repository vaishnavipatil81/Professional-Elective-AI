# =============================================
# 🌟 Best First Search Algorithm in Python
# =============================================

from queue import PriorityQueue

# Create a graph using dictionary
graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
    'J': [('E', 5), ('I', 3)]
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0  # Goal node
}

def best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))  # (heuristic, node)
    
    print("Path Traversal:")
    while not pq.empty():
        (h, current_node) = pq.get()
        print(current_node, end=" ")
        visited.add(current_node)
        
        if current_node == goal:
            print("\nGoal Reached!")
            return
        
        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))
                
    print("\nGoal Not Found!")

# Run the algorithm
start_node = 'A'
goal_node = 'J'
best_first_search(start_node, goal_node)
