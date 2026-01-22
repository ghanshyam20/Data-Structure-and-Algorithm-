# Chapter 2 , first excercise 

# i have do some  modification than in moodle , but it works same ,
from __future__ import annotations

import ctypes


class ReservedMemory:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("size must be positive")
        self._reserved_memory = ctypes.create_string_buffer(size)

    def __len__(self):
        return len(self._reserved_memory)

    def copy(self, src, count=None, src_i=0, dst_i=0):
        if count is None:
            count = len(src._reserved_memory) - src_i

        self._reserved_memory[dst_i:dst_i + count] = \
            src._reserved_memory[src_i:src_i + count]

    def __getitem__(self, i):
        return ord(self._reserved_memory[i])

    def __setitem__(self, i, v):
        self._reserved_memory[i] = v


class IntArray:
    def __init__(self, bytes_per_element=2):
        self._resmem = None
        self._size = 0
        self._bpe = bytes_per_element

        self._shift = 2 ** ((bytes_per_element * 8) - 1)
        self._min = -self._shift
        self._max = self._shift - 1

    def __len__(self):
        return self._size

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i < self._size:
            v = self[self._i]
            self._i += 1
            return v
        raise StopIteration

    def __repr__(self):
        if self._size == 0:
            return "Empty IntArray"
        return "IntArray (" + str(self._size) + " elements): [" + \
               ", ".join(str(v) for v in self) + "]"

    def __getitem__(self, index):
        val = 0
        for b in range(self._bpe):
            val |= self._resmem[index * self._bpe + b] << (8 * b)
        return val - self._shift

    def __setitem__(self, index, value):
        if value < self._min or value > self._max:
            raise TypeError("value out of range")

        value += self._shift
        for b in range(self._bpe):
            self._resmem[index * self._bpe + b] = (value >> (8 * b)) & 255

    def append(self, value):
        self._size += 1
        new_mem = ReservedMemory(self._size * self._bpe)

        if self._resmem:
            new_mem.copy(self._resmem)

        self._resmem = new_mem
        self[self._size - 1] = value

    def pop(self):
        if self._size == 0:
            return None

        v = self[self._size - 1]
        self._size -= 1

        if self._size == 0:
            self._resmem = None
        else:
            new_mem = ReservedMemory(self._size * self._bpe)
            new_mem.copy(self._resmem, self._size * self._bpe)
            self._resmem = new_mem

        return v

    # insert element at index
    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("wrong index")

        self._size += 1
        new_mem = ReservedMemory(self._size * self._bpe)

        if self._resmem:
            # copy before index
            new_mem.copy(self._resmem, index * self._bpe)

            # copy after index
            new_mem.copy(
                self._resmem,
                (self._size - index - 1) * self._bpe,
                index * self._bpe,
                (index + 1) * self._bpe
            )

        self._resmem = new_mem
        self[index] = value

    # search value and return index
    def search(self, value):
        i = 0
        while i < self._size:
            if self[i] == value:
                return i
            i += 1
        return -1
    

    
