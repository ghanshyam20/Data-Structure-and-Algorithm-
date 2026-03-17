from __future__ import annotations
import ctypes


class ReservedMemory:
    """
    this class is for making raw memory space
    """

    def __init__(self, size: int) -> None:
        # check size is int or not
        if not isinstance(size, int):
            raise TypeError('Memory size must be a positive integer > 0!')
        
        # check size limit (teacher gave this maybe)
        if not 1 <= size <= 65536:
            raise ValueError('Reserved memory size must be between 1 and 65536 bytes!')
        
        # create memory block
        self._reserved_memory = ctypes.create_string_buffer(size)

    def __len__(self) -> int:
        # return memory size
        return len(self._reserved_memory)

    def __repr__(self) -> str:
        # show memory content (just for debug)
        l = len(self._reserved_memory)
        plural = 's' if l > 1 else ''
        str_repr = f"[{', '.join(str(ord(i)) for i in self._reserved_memory)}]"
        return f"ReservedMemory ({l} byte{plural}): {str_repr}"

    def copy(self, mem_source,
             count=None,
             source_index=0,
             destination_index=0) -> None:
        # if count not given then copy full
        if count is None:
            count = len(mem_source._reserved_memory) - source_index

        # copying memory from one to another
        self._reserved_memory[
            destination_index:destination_index + count
        ] = mem_source._reserved_memory[
            source_index:source_index + count
        ]

    def __getitem__(self, k: int) -> int:
        # get value from memory
        return ord(self._reserved_memory[k])

    def __setitem__(self, k: int, val: int) -> None:
        # set value in memory
        self._reserved_memory[k] = val


class IntArray:
    """
    this is like list but we doing manually using memory
    """

    def __init__(self, bytes_per_element: int = 2) -> None:
        # start empty
        self._resmem = None
        self._size = 0
        self._bytes_per_element = bytes_per_element

        # calculate min max range
        self._shift_val = 2 ** ((bytes_per_element * 8) - 1)
        self._min_val = -self._shift_val
        self._max_val = self._shift_val - 1

    def __len__(self) -> int:
        # return size
        return self._size

    def __iter__(self):
        # for loop starting
        self._iter_index = 0
        return self

    def __next__(self):
        # give next value
        if self._iter_index < self._size:
            value = self[self._iter_index]
            self._iter_index += 1
            return value
        raise StopIteration

    def __repr__(self) -> str:
        # print nicely
        if self._size == 0:
            return "Empty IntArray"
        
        return f"IntArray ({self._size} elements): [{', '.join(str(v) for v in self)}]"

    def __getitem__(self, k: int) -> int:
        # getting number from memory
        stored_val = 0

        # combine bytes
        for byte_index in range(self._bytes_per_element):
            stored_val |= self._resmem[k * self._bytes_per_element + byte_index] << (8 * byte_index)

        return stored_val - self._shift_val

    def __setitem__(self, k: int, val: int) -> None:
        # check value valid or not
        if not isinstance(val, int) or not self._min_val <= val <= self._max_val:
            raise TypeError(f'Value must be an integer between {self._min_val} and {self._max_val}')

        # shifting value
        val_to_store = val + self._shift_val

        # break into bytes
        for byte_index in range(self._bytes_per_element):
            self._resmem[k * self._bytes_per_element + byte_index] = (
                val_to_store >> (8 * byte_index)
            ) & 255

    def append(self, val: int) -> None:
        # add value at end
        if not isinstance(val, int) or not self._min_val <= val <= self._max_val:
            raise TypeError('Invalid value')

        # increase size
        self._size += 1

        # make new memory bigger
        new_resmem = ReservedMemory(self._size * self._bytes_per_element)

        # copy old data
        if self._resmem:
            new_resmem.copy(self._resmem)

        self._resmem = new_resmem

        # set last value
        self[self._size - 1] = val

    def pop(self) -> int:
        # remove last value
        if self._size == 0:
            return None

        value = self[self._size - 1]
        self._size -= 1

        # resize memory
        if self._size == 0:
            self._resmem = None
        else:
            new_resmem = ReservedMemory(self._size * self._bytes_per_element)
            new_resmem.copy(self._resmem, self._size * self._bytes_per_element)
            self._resmem = new_resmem

        return value

    # remove element by index
    def remove(self, index: int) -> int:
        # if empty
        if self._size == 0:
            return None

        # check index correct
        if not isinstance(index, int) or not 0 <= index < self._size:
            raise IndexError('Index out of bounds')

        # save value
        removed_value = self[index]

        # decrease size
        self._size -= 1

        # if now empty
        if self._size == 0:
            self._resmem = None
            return removed_value

        # make new memory smaller
        new_resmem = ReservedMemory(self._size * self._bytes_per_element)

        # copy before index
        new_resmem.copy(
            self._resmem,
            count=index * self._bytes_per_element
        )

        # copy after index (shift left side)
        new_resmem.copy(
            self._resmem,
            count=(self._size - index) * self._bytes_per_element,
            source_index=(index + 1) * self._bytes_per_element,
            destination_index=index * self._bytes_per_element
        )

        self._resmem = new_resmem

        return removed_value
    

#This program creates a custom integer array
#  using memory instead of Python list and supports basic operations.