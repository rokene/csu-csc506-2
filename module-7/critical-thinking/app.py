#!/usr/bin/env python3

import heapq
import random

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

def generate_random_traffic_conditions(graph):
    for edge in graph.distances:
        graph.distances[edge] = random.randint(1, 10)

def main():
    graph = Graph()

    # Add nodes
    for node in range(1, 7):
        graph.add_node(node)

    # Add edges with initial weights
    edges = [
        (1, 2, 7), (1, 3, 9), (1, 6, 14),
        (2, 3, 10), (2, 4, 15),
        (3, 4, 11), (3, 6, 2),
        (4, 5, 6),
        (5, 6, 9)
    ]

    for edge in edges:
        graph.add_edge(*edge)

    print("Initial Traffic Conditions:")
    for edge, weight in graph.distances.items():
        print(f"Edge {edge}: {weight}")

    # Run Dijkstra's algorithm
    initial_node = 1
    visited, paths = dijkstra(graph, initial_node)
    print("\nShortest paths from node 1:")
    for destination, distance in visited.items():
        print(f"Node {destination} has distance {distance}")

    # Update traffic conditions
    generate_random_traffic_conditions(graph)
    print("\nUpdated Traffic Conditions:")
    for edge, weight in graph.distances.items():
        print(f"Edge {edge}: {weight}")

    # Re-run Dijkstra's algorithm with updated traffic conditions
    visited, paths = dijkstra(graph, initial_node)
    print("\nShortest paths from node 1 with updated traffic conditions:")
    for destination, distance in visited.items():
        print(f"Node {destination} has distance {distance}")

if __name__ == "__main__":
    main()
