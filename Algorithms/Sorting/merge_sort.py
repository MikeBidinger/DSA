def partition(arr, low, high):
    # Pivot is rightmost element
    piv = arr[high]
    i = low - 1
    # Traverse elements and compare with pivot
    for j in range(low, high):
        # Swap if element is smaller than pivot
        if arr[j] <= piv:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Swap pivot element with greater element
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # Return partition (pivot element) position
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # Finde pivot element
        piv = partition(arr, low, high)
        # Recursive call for left of pivot
        quick_sort(arr, low, piv - 1)
        # Recursive call for right of pivot
        quick_sort(arr, piv + 1, high)


if __name__ == "__main__":

    # Create an array
    arr = [64, 25, 12, 22, 11, 33]

    # Print array
    print("Original array:")
    print(arr)

    # Sort array
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:")
    print(arr)
