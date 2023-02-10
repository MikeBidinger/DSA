def fibonacci_search(arr, key):
    # Initialize Fibonacci numbers
    fib2, fib1, fib = 0, 1, 1
    # Find smallest Fibonacci nr greater than or equal to array length
    while fib < len(arr):
        fib2, fib1 = fib1, fib
        fib = fib2 + fib1
    # Search by decreasing the Fibonacci sequence
    left = -1
    while fib > 1:
        # Prevent list index out of range error
        i = min(left + fib2, len(arr) - 1)
        # Find sub-array (else found)
        if arr[i] < key:
            # -1 in Fibonacci sequence
            fib, fib1 = fib1, fib2
            fib2 = fib - fib1
            left = i
        elif arr[i] > key:
            # -2 in Fibonacci sequence
            fib, fib1 = fib2, fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    return -1


if __name__ == "__main__":

    # Create array
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    print("Input:")
    print("", arr)

    # Search element
    keys = [10, 50, 100, 123]
    for key in keys:
        index = fibonacci_search(arr, key)
        if index == -1:
            print("Element", key, "is not present in array")
        else:
            print("Element", key, "is present at index", index)
