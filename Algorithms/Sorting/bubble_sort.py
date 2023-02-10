def bubble_sort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr) - i - 1):
            # Swap the adjacent elements if previous element is smaller
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        # Break if there was no swap
        if swap == False:
            break


if __name__ == "__main__":

    # Create an array
    arr = [64, 25, 12, 22, 11]

    # Print array
    print("Original array:")
    print(arr)

    # Sort array
    bubble_sort(arr)
    print("Sorted array:")
    print(arr)
