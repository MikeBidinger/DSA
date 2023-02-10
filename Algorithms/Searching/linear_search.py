def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def linear_search_recursive(arr, key, size):
    if size == 0:
        return -1
    elif arr[size - 1] == key:
        return size - 1
    else:
        return linear_search_recursive(arr, key, size - 1)


if __name__ == "__main__":

    # Create array
    arr = [2, 3, 4, 10, 40]
    print("Input:")
    print("", arr)

    # Search element
    key = 12
    index = linear_search(arr, key)
    if index == -1:
        print("Element", key, "is not present in array")
    else:
        print("Element", key, "is present at index", index)

    # Search element recursively
    key = 10
    index = linear_search_recursive(arr, key, len(arr))
    if index == -1:
        print("Element", key, "is not present in array")
    else:
        print("Element", key, "is present at index", index)
