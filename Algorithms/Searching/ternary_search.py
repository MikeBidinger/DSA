def ternary_search(arr, key):
    left = 0
    right = len(arr) - 1
    while right >= left:
        # Divide array into three parts
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        # If key is at any mid
        if key == arr[mid1]:
            return mid1
        elif key == arr[mid2]:
            return mid2
        # Determine which part contains the key
        if key < arr[mid1]:
            right = mid1 - 1
        elif key > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return -1


def ternary_search_recursive(arr, key, left, right):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if key == arr[mid1]:
            return mid1
        elif key == arr[mid2]:
            return mid2
        if key < arr[mid1]:
            return ternary_search_recursive(arr, key, left, mid1 - 1)
        elif key > arr[mid2]:
            return ternary_search_recursive(arr, key, mid2 + 1, right)
        else:
            return ternary_search_recursive(arr, key, mid1 + 1, mid2 - 1)
    else:
        return -1


if __name__ == "__main__":

    # Create array
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Input:")
    print("", arr)

    # Search element
    keys = [1, 5, 10, 50]
    for key in keys:
        result = ternary_search(arr, key)
        if result == -1:
            print("Element", key, "is not present in array")
        else:
            print("Element", key, "is present at index", result)

    # Search element recursively
    keys = [1, 5, 10, 50]
    for key in keys:
        result = ternary_search_recursive(arr, key, 0, len(arr) - 1)
        if result == -1:
            print("Element", key, "is not present in array")
        else:
            print("Element", key, "is present at index", result)
