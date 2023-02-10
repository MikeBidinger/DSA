def countingSort(arr, input_range):
    # Sorted output array
    output = [0 for i in range(len(arr))]
    # Count array
    count = [0 for i in range(input_range)]
    # Count of each unique object
    for i in arr:
        count[ord(str(i))] += 1
    # Change count to position of object in output
    for i in range(input_range):
        count[i] += count[i - 1]
    # Build the output
    for i in range(len(arr)):
        output[count[ord(str(arr[i]))] - 1] = arr[i]
        count[ord(str(arr[i]))] -= 1
    return output


if __name__ == "__main__":

    # Create array
    arr = "#ilovetolearn!"
    arr = [9, 1, 4, 8, 6, 2, 7, 0]

    # Print array
    print("Original array:")
    print("", arr)

    # Sort array
    ans = countingSort(arr, 256)
    print("Sorted array:")
    print(" ", end="")
    for i in range(len(ans)):
        print(str(ans[i]), end="")
    print()
