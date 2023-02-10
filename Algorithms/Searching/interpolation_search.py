def interpolation_search(arr, key, left, right):
    while left <= right and key >= arr[left] and key <= arr[right]:
        # Find the position (uniform distribution)
        pos = left + (key - arr[left]) * (right - left) // (arr[right] - arr[left])
        if arr[pos] == key:
            return pos
        elif arr[pos] < key:
            left = pos + 1
        elif arr[pos] > key:
            right = pos - 1
    return -1


if __name__ == "__main__":

    # Create array
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    print("Input:")
    print("", arr)

    # Search element
    keys = [10, 21, 47, 100]
    for key in keys:
        index = interpolation_search(arr, key, 0, len(arr) - 1)
        if index == -1:
            print("Element", key, "is not present in array")
        else:
            print("Element", key, "is present at index", index)
