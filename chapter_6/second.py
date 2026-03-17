class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'


class HashTable:
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0

    def __repr__(self):
        text = ''

        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                text += ', ' + str(i) + ': ' + str(self.slots[i])

        if self.used_slots == 1:
            word = 'element'
        else:
            word = 'elements'

        return f'<HashTable ({self.used_slots} {word}): [{text.lstrip(", ")}]>'

    def _hash(self, key):
        # simple hash using sum of ascii
        total = 0
        for ch in key:
            total = total + ord(ch)
        return total % self.size

    def _find_free_slot(self, start):
        current = start

        while self.slots[current] is not None:
            current = current + 1

            if current >= self.size:
                current = 0

            if current == start:
                return None

        return current

    def _find_key(self, start, key):
        current = start

        while self.slots[current] is not None:
            if self.slots[current].key == key:
                return current

            current = current + 1

            if current >= self.size:
                current = 0

            if current == start:
                return None

        return None

    def put(self, key, value):
        index = self._hash(key)

        # check if key already exist
        key_index = self._find_key(index, key)

        if key_index is not None:
            self.slots[key_index].value = value
            return

        # find empty place
        free_index = self._find_free_slot(index)

        if free_index is None:
            raise MemoryError("HashTable is full")

        self.slots[free_index] = HashItem(key, value)
        self.used_slots += 1


