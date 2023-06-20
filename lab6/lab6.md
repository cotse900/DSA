# lab6
In this lab, you will implement the Dijkstra algorithm for finding shortest path on a graph using python

Define a function called dijkstra that will take the graph, start node, and target node as arguments and return the shortest path and its distance.
```def dijkstra(graph, start, target):```

The function should implement Dijkstra's algorithm using the following steps: 
1. Create a dictionary called distances that will store the distances between the start node and all other nodes in the graph. Set the distance of the start node to 0 and the distance of all other nodes to infinity:
```
distances = {node: float('inf') for node in graph}
distances[start] = 0
```
2. Create a dictionary called previous that will store the previous node in the shortest path to each node. Set the previous node of the start node to None.
```
previous = {node: None for node in graph}
```
3. Create a priority queue called unvisited that will store the unvisited nodes in the graph. Insert the start node with a priority of 0.
```
unvisited = [(0, start)]
```
4. While unvisited is not empty, do the following:

- i. Pop the node with the lowest priority from `unvisited`. If the node is the target node, stop the algorithm and return the shortest path and its distance.
- ii. For each neighbor of the current node, calculate the tentative distance from the start node to the neighbor. If the tentative distance is less than the current distance stored in `distances`, update `distances` and `previous`. Add the neighbor to `unvisited` with a priority equal to the tentative distance.
5. If the target node is not reached, return None.

putting it all together:
```
import heapq
def dijkstra(graph, start, target):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    unvisited = [(0, start)]
    previous = {node: None for node in graph}
   # complete the implementation of your code here
    
    return None
```
Use your implementation to calculate the shortest distance between A and F and B and G in the graph below
```
graph =
{
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 3},
    'D': {'B': 1, 'C': 4, 'E': 1, 'F': 2},
    'E': {'C': 3, 'D': 1, 'F': 1},
    'F': {'D': 2, 'E': 1, 'G': 3},
    'G': {'F': 3}
}
```
