def insertion_sort(array):
    # go from second element
    for i in range(1, len(array)):
        key = array[i]   # current value
        j = i - 1

        # move bigger elements to right
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1

        # put key in correct place
        array[j + 1] = key