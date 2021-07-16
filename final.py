from collections import defaultdict
import heapq
import math


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]


def a_star(graph, start, goal):
    open_set = [(0, start)]  # Heap queue with inital value (the start node)
    came_from = {}  # Keeps track of path from start to goal
    g_score = defaultdict(lambda: math.inf)  # A dictionary with infinity as the default value
    g_score[start] = 0  # Starting value is set to zero

    while (len(open_set) != 0):  # Repeats loop as long as open_set isn't empty
        _, current = heapq.heappop(open_set)  # Sets current to node label

        if current == goal:  # If we've reached the goal, then it builds the path
            return reconstruct_path(came_from, current)
        
        for neighbor, neighbor_d in graph[current]:  # Iterates through the node's neighbors
            tentative_g_score = g_score[current] + neighbor_d

            if tentative_g_score < g_score[neighbor]:  # Chooses the lower score between the two values
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score

                if neighbor not in open_set:  # Pushes the node to open_set if it's not already there
                    heapq.heappush(open_set, (neighbor_d, neighbor))
    return None  # If no path is found, None is returned
