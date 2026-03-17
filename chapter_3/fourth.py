class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        # store data and links
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode: {self.data}>'

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        # start empty list
        self._head = None
        self._tail = None
        self._size = 0

    def __repr__(self):
        # show all values
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        
        plural = '' if self._size == 1 else 's'
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        # return size of list
        return self._size

    def __iter__(self):
        # start loop from head
        self._iter_index = self._head
        return self

    def __next__(self):
        # give next value in loop
        if self._iter_index:
            value = self._iter_index.data
            self._iter_index = self._iter_index.next
            return value
        else:
            raise StopIteration
            
    def __getitem__(self, index):
        # check index valid or not
        if index < 0 or index >= self._size:
            raise ValueError('Index out of bounds')

        # go to index step by step
        current_node = self._head
        for i in range(index):
            current_node = current_node.next
        
        return current_node.data

    def __setitem__(self, index, value):
        # check index
        if index < 0 or index >= self._size:
            raise ValueError('Index out of bounds')

        # go to index
        current_node = self._head
        for i in range(index):
            current_node = current_node.next

        # set value
        current_node.data = value

    def append(self, value):
        # make new node
        new_node = ListNode(value, None, self._tail)

        # if list empty
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            # connect last node
            self._tail.next = new_node
            self._tail = new_node

        # increase size
        self._size = self._size + 1

    def pop(self):
        # if list empty
        if self._size == 0:
            return None
        
        node_to_remove = self._tail
        previous_node = node_to_remove.prev

        # if only one node
        if node_to_remove == self._head:
            self._head = None
        else:
            previous_node.next = None

        # update tail
        self._tail = previous_node

        # decrease size
        self._size = self._size - 1

        value = node_to_remove.data
        return value

    def contains(self, value):
        # check if value inside
        for node_value in self:
            if value == node_value:
                return True
        return False

    def clear(self):
        # remove all nodes one by one
        current_node = self._head
        while current_node:
            next_node = current_node.next
            current_node = next_node

        # reset everything
        self._head = None
        self._tail = None
        self._size = 0

    def insert(self, index, value):
        # check index is correct
        if index < 0 or index > self._size:
            raise ValueError('Index out of bounds')

        # create new node
        new_node = ListNode(value)

        # insert at front
        if index == 0:
            new_node.next = self._head

            if self._head is not None:
                self._head.prev = new_node

            self._head = new_node

            if self._tail is None:
                self._tail = new_node

        # insert at end
        elif index == self._size:
            new_node.prev = self._tail

            if self._tail is not None:
                self._tail.next = new_node

            self._tail = new_node

            if self._head is None:
                self._head = new_node

        # insert in middle
        else:
            current = self._head
            for i in range(index):
                current = current.next

            previous = current.prev

            # set links
            new_node.next = current
            new_node.prev = previous

            previous.next = new_node
            current.prev = new_node

        # increase size
        self._size = self._size + 1


# This code make a aoubly linked lsit where each node connect with prev and next we can add and 
#insert values by changing the linl betwween nodes
