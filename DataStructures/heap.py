from sys import maxsize as sys_maxsize


class Heap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [None] * (self.maxsize + 1)
        self.FRONT = 1

    def _parent(self, pos):
        return pos // 2

    def _left_child(self, pos):
        return 2 * pos

    def _right_child(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        return pos * 2 > self.size

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def _min_heapify(self, pos):
        if not self.isLeaf(pos):
            if self.heap[self._right_child(pos)] is not None:
                if (
                    self.heap[pos] > self.heap[self._left_child(pos)]
                    or self.heap[pos] > self.heap[self._right_child(pos)]
                ):
                    if (
                        self.heap[self._left_child(pos)]
                        < self.heap[self._right_child(pos)]
                    ):
                        self.swap(pos, self._left_child(pos))
                        self._min_heapify(self._left_child(pos))
                    else:
                        self.swap(pos, self._right_child(pos))
                        self._min_heapify(self._right_child(pos))
            else:
                if self.heap[pos] > self.heap[self._left_child(pos)]:
                    self.swap(pos, self._left_child(pos))
                    self._max_heapify(self._left_child(pos))

    def _max_heapify(self, pos):
        if not self.isLeaf(pos):
            if self.heap[self._right_child(pos)] is not None:
                if (
                    self.heap[pos] < self.heap[self._left_child(pos)]
                    or self.heap[pos] < self.heap[self._right_child(pos)]
                ):
                    if (
                        self.heap[self._left_child(pos)]
                        > self.heap[self._right_child(pos)]
                    ):
                        self.swap(pos, self._left_child(pos))
                        self._max_heapify(self._left_child(pos))
                    else:
                        self.swap(pos, self._right_child(pos))
                        self._max_heapify(self._right_child(pos))
            else:
                if self.heap[pos] < self.heap[self._left_child(pos)]:
                    self.swap(pos, self._left_child(pos))
                    self._max_heapify(self._left_child(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = element

    def print_heap(self):
        print(" ", self.heap[self.FRONT : self.size + 1])
        for i in range(1, (self.size // 2) + 1):
            print(
                " PARENT : "
                + str(self.heap[i])
                + " LEFT CHILD : "
                + str(self.heap[2 * i])
                + " RIGHT CHILD : "
                + str(self.heap[2 * i + 1])
            )

    def min_heap(self):
        self.heap[0] = -1 * sys_maxsize
        for pos in range(self.size // 2, 0, -1):
            self._min_heapify(pos)

    def max_heap(self):
        self.heap[0] = sys_maxsize
        for pos in range(self.size // 2, 0, -1):
            self._max_heapify(pos)

    def min_remove(self):
        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.heap[self.size] = None
        self.size -= 1
        self._min_heapify(self.FRONT)
        return popped

    def max_remove(self):
        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.heap[self.size] = None
        self.size -= 1
        self._max_heapify(self.FRONT)
        return popped


if __name__ == "__main__":

    # Create a min-heap
    heap = Heap(15)
    for x in [5, 3, 17, 10, 84, 19, 6, 22, 9]:
        heap.insert(x)
    heap.min_heap()
    """    3                5
         /   \            /   \ 
        5     6    =>    9     6
       / \   / \        / \   / \ 
      9  84 19 17      10 84 19 17
     / \              /
    22 10            22        """
    # Print min-heap
    print("MinHeap:")
    heap.print_heap()
    print("The minimum value is", heap.min_remove())
    print("MinHeap:")
    heap.print_heap()

    # Create to max-heap
    heap = Heap(15)
    for x in [5, 3, 17, 10, 84, 19, 6, 22, 9]:
        heap.insert(x)
    heap.max_heap()
    """     84                 22
          /    \             /    \ 
        22      19    =>    10    19
       /  \    /  \        / \    / \ 
      10   3  17   6      9   3  17  6
     /  \                /
    5    9              5          """
    # Print max-heap
    print("MaxHeap:")
    heap.print_heap()
    print("The maximum value is", heap.max_remove())
    print("MaxHeap:")
    heap.print_heap()
