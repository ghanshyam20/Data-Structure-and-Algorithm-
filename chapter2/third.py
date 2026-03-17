from __future__ import annotations
import ctypes


class ReservedMemory():
    # this class make raw memory space
    def __init__(self, size: int) -> None:
        # checking size is int or not
        if not isinstance(size, int):
            raise TypeError('Memory size must be a positive integer > 0!')
        
        # check size range (teacher maybe told this)
        if not 1 <= size <= 65536:
            raise ValueError('Reserved memory size must be between 1 and 65536 bytes!')
        
        # creating memory
        self._reserved_memory = ctypes.create_string_buffer(size)

    def __len__(self) -> int:
        # return size of memory
        return len(self._reserved_memory)

    def __repr__(self) -> str:
        # just showing memory values (for see)
        l = len(self._reserved_memory)
        plural = 's' if l > 1 else ''
        str_repr = f"[{', '.join(str(ord(i)) for i in self._reserved_memory)}]"
        return f"ReservedMemory ({l} byte{plural}): {str_repr}"

    def copy(self, mem_source,
             count=None,
             source_index=0,
             destination_index=0) -> None:
        # if count not given then take full
        if count is None:
            count = len(mem_source._reserved_memory) - source_index

        # copying memory data
        self._reserved_memory[
            destination_index:destination_index + count
        ] = mem_source._reserved_memory[
            source_index:source_index + count
        ]

    def __getitem__(self, k: int) -> int:
        # get value
        return ord(self._reserved_memory[k])

    def __setitem__(self, k: int, val: int) -> None:
        # set value
        self._reserved_memory[k] = val


class IntArray():
    # this is like list but we do manually memory
    def __init__(self, bytes_per_element: int = 2) -> None:
        # start empty
        self._resmem = None
        self._size = 0
        self._bytes_per_element = bytes_per_element

        # find min max range
        self._shift_val = 2 ** ((self._bytes_per_element * 8) - 1)
        self._min_val = -self._shift_val
        self._max_val = self._shift_val - 1

    def __len__(self) -> int:
        # return size
        return self._size

    def __iter__(self):
        # for loop start from 0
        self._iter_index = 0
        return self

    def __next__(self) -> int:
        # give next value
        if self._iter_index < self._size:
            self._iter_index += 1
            return self.__getitem__(self._iter_index - 1)
        else:
            # stop loop
            raise StopIteration

    def __repr__(self) -> str:
        # show array nicely
        if not self._resmem:
            return "Empty IntArray"
        
        l = self._size
        plural = 's' if l > 1 else ''
        str_repr = f"[{', '.join(str(v) for v in self)}]"
        return f"IntArray ({l} element{plural}): {str_repr}"

    def __setitem__(self, k: int, val: int) -> None:
        # check value ok or not
        if not isinstance(val, int) or not self._min_val <= val <= self._max_val:
            raise TypeError(f'Value must be an integer between {self._min_val} and {self._max_val}')

        # shift value
        val_to_store = val + self._shift_val

        # break into bytes
        for byte_index in range(self._bytes_per_element):
            self._resmem[k * self._bytes_per_element + byte_index] = (
                val_to_store >> (8 * byte_index)
            ) & 255

    def __getitem__(self, k: int) -> int:
        # read value from memory
        stored_val = 0

        # combine bytes
        for byte_index in range(self._bytes_per_element):
            stored_val |= self._resmem[k * self._bytes_per_element + byte_index] << (8 * byte_index)

        return stored_val - self._shift_val

    def append(self, val: int) -> None:
        # add value at end
        if not isinstance(val, int) or not self._min_val <= val <= self._max_val:
            raise TypeError('Invalid value')

        # increase size
        self._size += 1

        # new memory bigger
        new_resmem = ReservedMemory(self._size * self._bytes_per_element)

        # copy old data
        if self._resmem:
            new_resmem.copy(self._resmem)

        self._resmem = new_resmem

        # set last value
        self.__setitem__(self._size - 1, val)

    def pop(self) -> int:
        # remove last element
        if self._size == 0:
            return None

        val = self.__getitem__(self._size - 1)
        self._size -= 1

        # resize memory
        if self._size > 0:
            new_resmem = ReservedMemory(self._size * self._bytes_per_element)
            new_resmem.copy(self._resmem, count=self._size * self._bytes_per_element)
        else:
            new_resmem = None

        self._resmem = new_resmem

        return val

    # search value in array
    def search(self, value):
        # loop all elements
        for i in range(self._size):
            if self[i] == value:
                return i  # found index
        
        # not found
        return -1