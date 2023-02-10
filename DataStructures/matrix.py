from pprint import pprint as pp


class Matrix:
    def __init__(self, arr):
        self.arr = arr
        self.rows = len(arr)
        self.columns = len(arr[0])

    def print_matrix(self):
        # for i in range(self.rows):
        #     for j in range(self.columns):
        #         print(self.arr[i][j], end=" ")
        #     print("")
        pp(self.arr)

    def print_principal_diagonal(self):
        print("Principal Diagonal:")
        for i in range(self.rows):
            for j in range(self.columns):
                if i == j:
                    print(self.arr[i][j], end=" ")
        print()

    def print_secondary_diagonal(self):
        print("Secondary Diagonal:")
        n = max(self.rows, self.columns) - 1
        for i in range(self.rows):
            for j in range(self.columns):
                if i + j == n:
                    print(self.arr[i][j], end=" ")
        print()

    def search_matrix(self, val):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.arr[i][j] == val:
                    return True
        return False

    def search_sorted_matrix(self, val):
        for i in range(self.rows):
            if self.arr[i][0] > val:
                for j in range(self.columns):
                    if self.arr[i - 1][j] == val:
                        return True
            elif i == self.rows - 1:
                for j in range(self.columns):
                    if self.arr[i][j] == val:
                        return True
        return False

    def sort_matrix(self, ascending=True):
        temp = [0] * self.rows * self.columns
        k = 0
        for i in range(self.rows):
            for j in range(self.columns):
                temp[k] = self.arr[i][j]
                k += 1
        temp.sort(reverse=not (ascending))
        k = 0
        for i in range(self.rows):
            for j in range(self.columns):
                self.arr[i][j] = temp[k]
                k += 1

    def transpose(self):
        for i in range(self.rows):
            for j in range(i, self.columns):
                self.arr[i][j], self.arr[j][i] = self.arr[j][i], self.arr[i][j]

    def reverse_columns(self):
        for j in range(self.columns):
            k = self.rows
            for i in range(self.rows):
                if i < k:
                    k -= 1
                    self.arr[i][j], self.arr[k][j] = self.arr[k][j], self.arr[i][j]
                else:
                    break

    def rotate_180(self):
        if self.rows == self.columns:
            self.transpose()
            self.reverse_columns()
            self.transpose()
            self.reverse_columns()

    def get_unique(self):
        uniques = []
        elements = {}
        for i in range(self.rows):
            for j in range(self.columns):
                if self.arr[i][j] in elements:
                    elements[self.arr[i][j]] += 1
                else:
                    elements[self.arr[i][j]] = 1
        for x in elements:
            if elements[x] == 1:
                uniques.append(x)
        return uniques


if __name__ == "__main__":

    # Create matrix
    arr = Matrix([[8, 6, 7, 5], [4, 2, 1, 3], [9, 12, 11, 10]])

    # Print matrix
    print("Original Matrix:")
    arr.print_matrix()

    # Sort matrix
    arr.sort_matrix(ascending=False)
    print("Descending Sorted Matrix:")
    arr.print_matrix()
    arr.sort_matrix()
    print("Ascending Sorted Matrix:")
    arr.print_matrix()

    # Create matrix
    arr = Matrix([[4, 3, 2, 1], [3, 2, 1, 4], [2, 1, 5, 1], [1, 4, 3, 6]])

    # Print matrix diagonals
    arr.print_principal_diagonal()
    arr.print_secondary_diagonal()

    # Search matrix
    val = 6
    print(val, "in Matrix:", arr.search_matrix(val))
    print(val, "in Matrix:", arr.search_sorted_matrix(val))

    # Rotate matrix 180 degree
    arr.print_matrix()
    arr.rotate_180()
    arr.print_matrix()

    # Search unique elements in matrix
    print("Unique elements:", arr.get_unique())
