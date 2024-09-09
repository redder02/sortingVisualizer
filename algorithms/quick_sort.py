def quick_sort(arr, visualize_func):
    quick_sort_recursive(arr, 0, len(arr) - 1, visualize_func)

def quick_sort_recursive(arr, low, high, visualize_func):
    if low < high:
        pi = partition(arr, low, high, visualize_func)
        quick_sort_recursive(arr, low, pi - 1, visualize_func)
        quick_sort_recursive(arr, pi + 1, high, visualize_func)

def partition(arr, low, high, visualize_func):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            visualize_func(arr)  # Visualize after each swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    visualize_func(arr)  # Visualize the pivot swap
    return i + 1
