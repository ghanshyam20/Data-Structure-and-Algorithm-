def binary_search_iterative(array, value):
    # set start and end
    left = 0
    right = len(array) - 1

    # loop while valid range
    while left <= right:
        mid = (left + right) // 2

        # check middle
        if array[mid] == value:
            return mid

        # go right side
        elif array[mid] < value:
            left = mid + 1

        # go left side
        else:
            right = mid - 1

    return None   # not found