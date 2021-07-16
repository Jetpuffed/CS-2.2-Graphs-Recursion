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
    open_set = [(0, start)]
    came_from = {}
    g_score = defaultdict(lambda: math.inf)
    g_score[start] = 0

    while (len(open_set) != 0):
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor, neighbor_d in graph[current]:
            tentative_g_score = g_score[current] + neighbor_d

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score

                if neighbor not in open_set:
                    heapq.heappush(open_set, (neighbor_d, neighbor))
    return None
