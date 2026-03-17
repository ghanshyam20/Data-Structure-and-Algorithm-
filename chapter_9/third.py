def heap_sort(array):
    n = len(array)

    # build max heap
    i = n // 2 - 1
    while i >= 0:
        sift_down(array, i, n - 1)
        i = i - 1

    # sort the array
    end = n - 1
    while end > 0:
        # swap first and last
        temp = array[0]
        array[0] = array[end]
        array[end] = temp

        # fix heap
        sift_down(array, 0, end - 1)

        end = end - 1