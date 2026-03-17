class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        # store value and links
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
        # show list
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        
        plural = '' if self._size == 1 else 's'
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        # return size
        return self._size

    def __iter__(self):
        # start loop
        self._iter_index = self._head
        return self

    def __next__(self):
        # give next value
        if self._iter_index:
            value = self._iter_index.data
            self._iter_index = self._iter_index.next
            return value
        else:
            raise StopIteration
            
    def __getitem__(self, index):
        # check index
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))

        current_node = self._head
        for i in range(index):
            current_node = current_node.next
        
        return current_node.data

    def __setitem__(self, index, value):
        # check index
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))

        current_node = self._head
        for i in range(index):
            current_node = current_node.next

        current_node.data = value

    def append(self, value):
        # make new node
        new_node = ListNode(value, None, self._tail)

        # if empty
        if self._head is None:
            self._head = self._tail = new_node
        else:
            # connect last
            self._tail.next = new_node
            self._tail = new_node

        # inc size
        self._size += 1

    def pop(self):
        # if empty
        if not self._size:
            return None
        
        node_to_remove = self._tail
        previous_node = node_to_remove.prev

        # if only one
        if node_to_remove == self._head:
            self._head = None
        else:
            previous_node.next = None

        self._tail = previous_node

        self._size -= 1
        value = node_to_remove.data
        return value

    def insert(self, index, value):
        # check index ok or not
        if index < 0 or index > self._size:
            raise(ValueError('Index out of bounds'))

        previous_node = None
        next_node = self._head

        # move to position
        for i in range(index):
            previous_node = next_node
            next_node = next_node.next

        # make node
        new_node = ListNode(value, next_node, previous_node)

        # if first
        if previous_node is None:
            self._head = new_node
        else:
            previous_node.next = new_node
        
        # if last
        if next_node is None:
            self._tail = new_node
        else:
            next_node.prev = new_node

        # inc size
        self._size += 1

    def remove_by_value(self, value):
        # find value
        current_node = self._head
        index = 0

        while current_node and current_node.data != value:
            current_node = current_node.next
            index += 1
        
        # not found
        if not current_node:
            return None

        previous_node = current_node.prev
        next_node = current_node.next

        # if first
        if previous_node is None:
            self._head = next_node
        else:
            previous_node.next = next_node

        # if last
        if next_node is None:
            self._tail = previous_node
        else:
            next_node.prev = previous_node

        self._size -= 1
        return index

    def contains(self, value):
        # check exist or not
        for node_value in self:
            if value == node_value:
                return True
        return False

    def clear(self):
        # remove all
        current_node = self._head
        while current_node:
            next_node = current_node.next
            current_node = next_node

        self._head = None
        self._tail = None
        self._size = 0

    def remove(self, index):
        # check index
        if index < 0 or index >= self._size:
            raise ValueError('Index out of bounds')

        # if empty
        if self._size == 0:
            return None

        # go to node
        current = self._head
        for i in range(index):
            current = current.next

        value = current.data

        prev_node = current.prev
        next_node = current.next

        # first node
        if prev_node is None:
            self._head = next_node
        else:
            prev_node.next = next_node

        # last node
        if next_node is None:
            self._tail = prev_node
        else:
            next_node.prev = prev_node

        self._size -= 1

        return value
    

#this code make double linked list hwere nodes conenct with next and prev we can add , insert
# and removevaluese by changing the links between nodes

