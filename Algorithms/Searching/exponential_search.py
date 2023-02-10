def binary_search(arr, key, left, right):
    if left <= right:
        mid = (right + left) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, key, left, mid - 1)
        else:
            return binary_search(arr, key, mid + 1, right)
    else:
        return -1


def exponential_search(arr, key):
    if arr[0] == key:
        return 0
    # Find sub-array exponentially for binary search
    i = 1
    while i < len(arr) and arr[i] <= key:
        i = i * 2
    # Apply binary search on found sub-array
    return binary_search(arr, key, i // 2, min(i, len(arr) - 1))


if __name__ == "__main__":

    # Create array
    arr = [2, 3, 4, 10, 40]
    print("Input:")
    print("", arr)

    # Search element
    keys = [2, 4, 40]
    for key in keys:
        index = exponential_search(arr, key, 0, len(arr) - 1)
        if index == -1:
            print("Element", key, "is not present in array")
        else:
            print("Element", key, "is present at index", index)
