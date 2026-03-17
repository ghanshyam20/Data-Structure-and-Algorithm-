def sift_down(array, start, end):
    # start from given index
    root = start

    while True:
        left = 2 * root + 1
        right = 2 * root + 2

        largest = root

        # check left child
        if left <= end and array[left] > array[largest]:
            largest = left

        # check right child
        if right <= end and array[right] > array[largest]:
            largest = right

        # if no change stop
        if largest == root:
            break

        # swap values
        temp = array[root]
        array[root] = array[largest]
        array[largest] = temp

        # move down
        root = largest