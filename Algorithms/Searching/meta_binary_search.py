from math import log2


def meta_binary_search(arr, key):
    n = len(arr)
    # Number of bits of lagest array index
    bits = int(log2(n - 1)) + 1
    # Set left position of array index
    left = 0
    for i in range(bits - 1, -1, -1):
        if arr[left] == key:
            return left
        # Set right position of array index
        right = left | (1 << i)
        # Determine which half contains the key
        if right < n and arr[right] <= key:
            left = right
    if arr[left] == key:
        return left
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
        index = meta_binary_search(arr, key)
        if index == -1:
            print("Element", key, "is not present in array")
        else:
            print("Element", key, "is present at index", index)
