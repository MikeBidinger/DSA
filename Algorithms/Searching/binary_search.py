def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    # Divide array in half (repeatedly)
    while left < right:
        mid = (right + left) // 2
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid
    if arr[left] == key:
        return left
    elif arr[right] == key:
        return right
    return -1


def binary_search_recursive(arr, key, left, right):
    if left <= right:
        mid = (right + left) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search_recursive(arr, key, left, mid - 1)
        else:
            return binary_search_recursive(arr, key, mid + 1, right)
    else:
        return -1


if __name__ == "__main__":

    # Create array
    arr = [-2, 10, 100, 250, 32315]
    print("Input:")
    print("", arr)

    # Search element
    keys = [-2, 100, 32315, 123]
    for key in keys:
        index = binary_search(arr, key)
        if index == -1:
            print("Element", key, "is not present in array")
        else:
            print("Element", key, "is present at index", index)

    # Search element recursively
    keys = [-2, 100, 32315, 123]
    for key in keys:
        index = binary_search_recursive(arr, key, 0, len(arr) - 1)
        if index == -1:
            print("Element", key, "is not present in array")
        else:
            print("Element", key, "is present at index", index)
