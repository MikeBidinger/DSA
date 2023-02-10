def sentinel_search(arr, key):
    n = len(arr)
    # Last element of the array
    last = arr[n - 1]
    # Place element to be searched at the last index
    arr[n - 1] = key
    i = 0
    while arr[i] != key:
        i += 1
    # Put the last element back
    arr[n - 1] = last
    if i < n - 1 or arr[n - 1] == key:
        return i
    return -1


if __name__ == "__main__":

    # Create array
    arr = [-2, 10, 100, 250, 32315]
    print("Input:")
    print("", arr)

    # Search element
    keys = [-2, 100, 32315, 123]
    for key in keys:
        index = sentinel_search(arr, key)
        if index == -1:
            print("Element", key, "is not present in array")
        else:
            print("Element", key, "is present at index", index)
