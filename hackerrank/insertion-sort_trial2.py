def insertionSort1(n, arr):
    # Write your code here
    key = arr[n-1]
    i = n - 2
    # shift elements greater than key to the right
    while i >= 0 and arr[i] > key:
        arr[i+1] = arr[i]
        print(" ".join(str(x) for x in arr))
        i -= 1
    # place key in its final spot
    arr[i+1] = key
    print(" ".join(str(x) for x in arr))