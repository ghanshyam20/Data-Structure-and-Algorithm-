def interpolation_search(array, value):
    # set start and end
    low = 0
    high = len(array) - 1

    # loop while valid range and value inside range
    while low <= high and value >= array[low] and value <= array[high]:

        # avoid division by zero
        if array[high] == array[low]:
            if array[low] == value:
                return low
            else:
                return None

        # estimate position
        pos = low + ( (value - array[low]) * (high - low) ) // (array[high] - array[low])

        # check position valid
        if pos < 0 or pos >= len(array):
            return None

        # found
        if array[pos] == value:
            return pos

        # go right
        if array[pos] < value:
            low = pos + 1
        else:
            # go left
            high = pos - 1

    return None