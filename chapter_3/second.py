class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
    def __init__(self):
        # starting empty list
        self._head = None
        self._tail = None
        self._size = 0

    def __repr__(self):
        # show all values in list
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        # return how many items
        return self._size

    def append(self, value):
        # make new node
        new_node = ListNode(value)

        # if list is empty
        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            # connect last node to new one
            self._tail.next = new_node
            self._tail = new_node

        # increase size
        self._size += 1

    def pop(self):
        # if list empty return nothing
        if self._size == 0:
            return None

        # if only one item in list
        if self._size == 1:
            val = self._head.data
            self._head = None
            self._tail = None
            self._size = 0
            return val

        # more then one item
        current = self._head

        # go to second last node
        while current.next != self._tail:
            current = current.next

        # get last value
        val = self._tail.data

        # remove last node
        self._tail = current
        self._tail.next = None

        # decrease size
        self._size -= 1

        return val