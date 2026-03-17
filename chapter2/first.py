from __future__ import annotations
import ctypes


class ReservedMemory:
    def __init__(self, size: int) -> None:
        # check if size is correct
        if type(size) != int:
            raise TypeError(" bro Memory size must be int")
        if size <= 0:
            raise ValueError("Memory size must be > 0")

        # make empty memory space
        self._reserved_memory = ctypes.create_string_buffer(size)

    def __len__(self) -> int:
        # return total size
        return len(self._reserved_memory)

    def copy(self, source, count=None, source_index=0, destination_index=0) -> None:
        # if count not given, copy all
        if count is None:
            count = len(source._reserved_memory) - source_index

        # copy data from one place to another
        self._reserved_memory[destination_index:destination_index + count] = \
            source._reserved_memory[source_index:source_index + count]

    def __getitem__(self, k: int) -> int:
        # get value from memory
        return ord(self._reserved_memory[k])

    def __setitem__(self, k: int, val: int) -> None:
        # set value in memory
        self._reserved_memory[k] = val


class IntArray:
    def __init__(self, bytes_per_element: int = 2) -> None:
        # start empty
        self._resmem = None
        self._size = 0
        self._bytes_per_element = bytes_per_element

        # find range of numbers
        self._shift_val = 2 ** ((bytes_per_element * 8) - 1)
        self._min_val = -self._shift_val
        self._max_val = self._shift_val - 1

    def __len__(self) -> int:
        # return how many elements
        return self._size

    def __iter__(self):
        # start loop from 0
        self._i = 0
        return self

    def __next__(self):
        # give next value
        if self._i < self._size:
            value = self[self._i]
            self._i += 1
            return value
        else:
            # stop loop
            raise StopIteration

    def __repr__(self) -> str:
        # show array nicely
        if self._size == 0:
            return "Empty IntArray"

        result = []
        for v in self:
            result.append(str(v))

        return "IntArray (" + str(self._size) + " elements): [" + ", ".join(result) + "]"

    def __getitem__(self, k: int) -> int:
        # this will  read number from memory
        stored = 0

        for b in range(self._bytes_per_element):
            stored = stored | (self._resmem[k * self._bytes_per_element + b] << (8 * b))

        return stored - self._shift_val

    def __setitem__(self, k: int, val: int) -> None:
        # check value range
        if val < self._min_val or val > self._max_val:
            raise TypeError("Value out of range")

        v = val + self._shift_val

        # break number into small  bytes
        for b in range(self._bytes_per_element):
            self._resmem[k * self._bytes_per_element + b] = (v >> (8 * b)) & 255

    def append(self, val: int) -> None:
        #  this add new value at end
        if val < self._min_val or val > self._max_val:
            raise TypeError("Value out of range")

        self._size = self._size + 1

        # make new memory
        new_mem = ReservedMemory(self._size * self._bytes_per_element)

        # copy old data
        if self._resmem is not None:
            new_mem.copy(self._resmem)

        self._resmem = new_mem

        # set last value
        self[self._size - 1] = val

    def pop(self):
        # it remove last value
        if self._size == 0:
            return None

        val = self[self._size - 1]
        self._size = self._size - 1

        #  its resize memory
        if self._size == 0:
            self._resmem = None
        else:
            new_mem = ReservedMemory(self._size * self._bytes_per_element)
            new_mem.copy(self._resmem, self._size * self._bytes_per_element)
            self._resmem = new_mem

        return val

    def insert(self, index: int, val: int) -> None:
        # insert value at position
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        if val < self._min_val or val > self._max_val:
            raise TypeError("Value out of range")

        self._size = self._size + 1

        # new memory bigger
        new_mem = ReservedMemory(self._size * self._bytes_per_element)

        # copy before index
        if self._resmem is not None:
            new_mem.copy(self._resmem, index * self._bytes_per_element)

            # copy after index
            new_mem.copy(
                self._resmem,
                (self._size - index - 1) * self._bytes_per_element,
                index * self._bytes_per_element,
                (index + 1) * self._bytes_per_element,
            )

        self._resmem = new_mem

        # put new value
        self[index] = val


#This code creates a custom integer array without using normal Python list.
#It uses low-level memory (ctypes) to store numbers manually.


