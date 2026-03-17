class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        # move last element up until correct place

        i = self._size - 1   # last index

        # go up while not root
        while i > 0:
            parent = (i - 1) // 2   # find parent index

            # if smaller than parent then swap
            if self._heap[i] < self._heap[parent]:
                temp = self._heap[i]
                self._heap[i] = self._heap[parent]
                self._heap[parent] = temp

                i = parent   # move up
            else:
                break   # stop if already correct