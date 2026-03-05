def pivot_sort(arr):
    """
    Sorts an array in ascending order using a pivot-based sorting algorithm (quicksort variant).
    
    This implementation uses the middle element as the pivot and partitions the array
    into three parts: elements less than the pivot, equal to the pivot, and greater than
    the pivot. The algorithm then recursively sorts the left and right partitions.
    
    Args:
        arr (list): A list of comparable elements to be sorted.
        
    Returns:
        list: A new sorted list in ascending order.
        
    Example:
        >>> pivot_sort([5, 2, 8, 1, 9])
        [1, 2, 5, 8, 9]
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Partition array into three parts using middle element as pivot
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort left and right partitions, concatenate with middle
    return pivot_sort(left) + middle + pivot_sort(right)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

