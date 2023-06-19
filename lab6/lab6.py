# DSA456V1A
# Lab 6
# Student: Chungon Tse
# ID: 154928188
# Date: 12 Apr 2023
# Dijkstra

import heapq


def dijkstra(graph, start, target):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    unvisited = [(0, start)]
    previous = {node: None for node in graph}

    while unvisited:
        current_distance, current_node = heapq.heappop(unvisited)
        if current_node == target:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous[current_node]
            path.reverse()
            return path, current_distance

        for neighbor, priority in graph[current_node].items():
            tentative_distance = current_distance + priority
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                previous[neighbor] = current_node
                heapq.heappush(unvisited, (tentative_distance, neighbor))

    return None


graph2 = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 3},
    'D': {'B': 1, 'C': 4, 'E': 1, 'F': 2},
    'E': {'C': 3, 'D': 1, 'F': 1},
    'F': {'D': 2, 'E': 1, 'G': 3},
    'G': {'F': 3}
}

shortest_distance = dijkstra(graph2, 'A', 'F')
print("Shortest distance from A to F:", shortest_distance)
shortest_distance = dijkstra(graph2, 'B', 'G')
print("Shortest distance from B to G:", shortest_distance)
