from collections import defaultdict


class Graph:
    # This class represents a directed graph using adjacency list representation
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printBFS(self, v):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        # Create a queue for BFS
        q = []
        # Mark the source vertice as visited and enqueue it
        q.append(v)
        visited[v] = True
        while q:
            # Dequeue a vertex from queue and print it
            v = q.pop(0)
            print(v, end=" ")
            # Get all adjacent vertices of the dequeued vertex v
            # If a adjacent has not been visited, then mark it visited and enqueue it
            for i in self.graph[v]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True

    def recursiveDFS(self, v, visited):
        # Mark vertice as visited
        visited[v] = True
        print(v, end=" ")
        # Go as far as possible along branch for not visited vertices
        for i in self.graph[v]:
            if visited[i] == False:
                self.recursiveDFS(i, visited)

    def printDFS(self, v):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        self.recursiveDFS(v, visited)


if __name__ == "__main__":

    # Create a graph
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print(g.graph)

    # Print Breath-First Search
    print("Following is Breadth-First Search (starting from vertex 2)")
    g.printBFS(2)
    print()

    # Print Breath-First Search
    print("Following is Depth-First Search (starting from vertex 2)")
    g.printDFS(2)
    print()
