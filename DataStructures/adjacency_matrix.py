from pprint import pprint as pp


class AdjMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0 for i in range(vertices)] for j in range(vertices)]

    def add_edge(self, src, dest):
        self.matrix[src][dest] = 1
        self.matrix[dest][src] = 1

    def print_matrix(self):
        pp(self.matrix)


if __name__ == "__main__":

    # Creat adjacency matrix
    adjMat = AdjMatrix(5)

    # Set edge
    adjMat.add_edge(0, 2)
    adjMat.add_edge(1, 4)

    # Print adjacency matrix
    adjMat.print_matrix()
