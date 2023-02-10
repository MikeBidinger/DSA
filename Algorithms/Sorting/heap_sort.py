def max_heapify(arr, N, i):
    largest = i
    l_child = 2 * i + 1
    r_child = 2 * i + 2
    if l_child < N and arr[largest] < arr[l_child]:
        largest = l_child
    if r_child < N and arr[largest] < arr[r_child]:
        largest = r_child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, N, largest)


def min_heapify(arr, N, i):
    smallest = i
    l_child = 2 * i + 1
    r_child = 2 * i + 2
    if l_child < N and arr[smallest] > arr[l_child]:
        smallest = l_child
    if r_child < N and arr[smallest] > arr[r_child]:
        smallest = r_child
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, N, smallest)


def heap_sort(arr, max=True):
    # Heapify
    for i in range(len(arr) // 2 - 1, -1, -1):
        if max:
            max_heapify(arr, len(arr), i)
        else:
            min_heapify(arr, len(arr), i)
    # Sort
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        if max:
            max_heapify(arr, i, 0)
        else:
            min_heapify(arr, i, 0)


if __name__ == "__main__":

    # Create an array
    arr = [64, 25, 12, 22, 11, 33]
    # arr = [12, 11, 13, 5, 6, 7]

    # Print array
    print("Original array:")
    print(arr)

    # Sort array ascending (max-heap)
    heap_sort(arr)
    print("Ascending sorted array:")
    print(arr)

    # Sort array descending (min-heap)
    heap_sort(arr, False)
    print("Descending sorted array:")
    print(arr)
