def insertion_sort(arr, visualize_func):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            visualize_func(arr)  # Visualize each swap
        arr[j + 1] = key
        visualize_func(arr)  # Visualize after insertion
