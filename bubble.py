def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Flag to optimize the algorithm by checking if any swaps were made
        swapped = False

        for j in range(n - 1 - i):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps were made in this pass, the list is already sorted
        if not swapped:
            break

    return arr

# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)
