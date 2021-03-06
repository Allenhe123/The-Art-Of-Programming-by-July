def binarySearch(lst, n):
    low, high = 0, len(lst) - 1     # high value is len(lst) -1
    while low <= high:                # <=
        mid = (low + high) / 2
        if lst[mid] > n:
            high = mid - 1          # +-1
        elif lst[mid] < n:
            low = mid + 1
        else:
            return mid
    return None
