def merge_sort(arr, visualize_func):
    merge_sort_recursive(arr, 0, len(arr) - 1, visualize_func)

def merge_sort_recursive(arr, left, right, visualize_func):
    if left < right:
        middle = (left + right) // 2
        merge_sort_recursive(arr, left, middle, visualize_func)
        merge_sort_recursive(arr, middle + 1, right, visualize_func)
        merge(arr, left, middle, right, visualize_func)

def merge(arr, left, middle, right, visualize_func):
    L = arr[left:middle + 1]
    R = arr[middle + 1:right + 1]

    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        visualize_func(arr)  # Visualize the array after each change

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
        visualize_func(arr)

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        visualize_func(arr)
