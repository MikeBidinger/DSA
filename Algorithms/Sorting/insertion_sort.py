def insertion_sort(arr):
    for i in range(1, len(arr)):
        # Temporarily take element from array
        val = arr[i]
        j = i - 1
        # Keep shifting elements while the temp element is smaller
        while j >= 0 and val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert element back into correct position in the array
        arr[j + 1] = val


if __name__ == "__main__":

    # Create an array
    arr = [64, 25, 12, 22, 11]

    # Print array
    print("Original array:")
    print(arr)

    # Sort array
    insertion_sort(arr)
    print("Sorted array:")
    print(arr)
