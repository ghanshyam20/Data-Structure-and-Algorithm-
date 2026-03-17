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

        for index in range(len(self.slots)):
            slot = self.slots[index]
            if slot is not None:
                text += f', {index}: {slot}'

        if self.used_slots == 1:
            word = 'element'
        else:
            word = 'elements'

        return f'<HashTable ({self.used_slots} {word}): [{text.lstrip(", ")}]>'

    def _hash(self, key):
        # simple hash based on key length
        return len(key) % self.size

    def _find_free_slot(self, start):
        current = start

        while True:
            if self.slots[current] is None:
                return current

            current = current + 1
            if current >= self.size:
                current = 0

            if current == start:
                return None