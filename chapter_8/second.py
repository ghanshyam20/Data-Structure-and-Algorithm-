class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        index = self._size - 1
        parent_index = (index - 1) // 2

        while index > 0 and self._heap[index] < self._heap[parent_index]:
            temp = self._heap[index]
            self._heap[index] = self._heap[parent_index]
            self._heap[parent_index] = temp

            index = parent_index
            parent_index = (index - 1) // 2

    def insert(self, value):
        self._heap.append(value)
        self._size += 1
        self._float()

    def _sink(self):
        # move root down until correct place

        index = 0   # start from root

        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            smallest = index

            # check left child
            if left < self._size:
                if self._heap[left] < self._heap[smallest]:
                    smallest = left

            # check right child
            if right < self._size:
                if self._heap[right] < self._heap[smallest]:
                    smallest = right

            # if no change stop
            if smallest == index:
                break

            # swap with smaller child
            temp = self._heap[index]
            self._heap[index] = self._heap[smallest]
            self._heap[smallest] = temp

            index = smallest   # move down