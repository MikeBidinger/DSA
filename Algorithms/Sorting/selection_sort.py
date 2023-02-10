def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            # Select smallest element from the unsorted portion of the array
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Swap elements
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":

    # Create an array
    arr = [64, 25, 12, 22, 11]

    # Print array
    print("Original array:")
    print(arr)

    # Sort array
    selection_sort(arr)
    print("Sorted array:")
    print(arr)
