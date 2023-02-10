def countingSort(arr, pos, string_input=False):
    # Sorted output array
    output = [0 for i in range(len(arr))]
    # Count array
    if string_input:
        count = [0 for i in range(256)]
    else:
        count = [0 for i in range(10)]
    # Count of each unique object
    for i in range(len(arr)):
        if string_input:
            char_num = ord(arr[i][pos].lower())
            count[char_num] += 1
        else:
            index = arr[i] // pos
            count[index % 10] += 1
    # Change count to position of object in output
    if string_input:
        for i in range(256):
            count[i] += count[i - 1]
    else:
        for i in range(1, 10):
            count[i] += count[i - 1]
    # Build the output
    for i in range(len(arr) - 1, -1, -1):
        if string_input:
            char_num = ord(arr[i][pos].lower())
            output[count[char_num] - 1] = arr[i]
            count[char_num] -= 1
        else:
            index = arr[i] // pos
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
    # Copy output to given array
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    max_number = max(arr)
    decimal_pos = 1
    while max_number / decimal_pos >= 1:
        countingSort(arr, decimal_pos)
        print("  -", decimal_pos, arr)
        decimal_pos *= 10


def radixSortString(arr):
    max_length = 0
    for x in arr:
        if len(x) > max_length:
            max_length = len(x)
    for char_pos in range(max_length - 1, -1, -1):
        countingSort(arr, char_pos, string_input=True)
        print("  -", char_pos, arr)
        char_pos += 1


if __name__ == "__main__":

    # Create integer array
    arr = [170, 45, 75, 90, 802, 24, 2, 66]

    # Print array
    print("Original integer array:")
    print("", arr)

    # Sort array
    radixSort(arr)
    print("Sorted integer array:")
    print("", arr)

    # Create string array
    arr = ["BCDEF", "dbaqc", "abcde", "bbbbb"]

    # Print array
    print("Original string array:")
    print("", arr)

    # Sort array
    radixSortString(arr)
    print("Sorted string array:")
    print("", arr)
