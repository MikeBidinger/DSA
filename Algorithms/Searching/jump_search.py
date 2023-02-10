from math import sqrt


def jump_search(arr, key):
    # Optimal jump value
    m = int(sqrt(len(arr)))
    # Find start position (closest to and less than key)
    pos = 0
    for i in range(0, len(arr), m):
        if arr[i] >= key:
            break
        pos = i
    # Linear search from start position
    for i in range(pos, len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":

    # Create array
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 55, 77, 89, 101, 201, 256, 780]
    print("Input:")
    print("", arr)

    # Search element
    keys = [0, 21, 780, 1000]
    for key in keys:
        index = jump_search(arr, key)
        if index == -1:
            print("Element", key, "is not present in array")
        else:
            print("Element", key, "is present at index", index)
