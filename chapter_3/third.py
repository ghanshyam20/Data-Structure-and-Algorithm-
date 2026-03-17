class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
    def __init__(self):
        # start empty
        self._head = None
        self._tail = None
        self._size = 0

    def __repr__(self):
        # print list values
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        # return size
        return self._size

    def append(self, value):
        # create new node
        new_node = ListNode(value)

        # if empty list
        if self._head is None:
            self._head = self._tail = new_node
        else:
            # connect last to new
            self._tail.next = new_node
            self._tail = new_node
        
        # increase size
        self._size += 1

    def pop(self):
        # if empty
        if not self._size:
            return None
        
        # if one item
        if self._size == 1:
            previous_node = None
        else:
            # go to second last
            previous_node = self._head
            for _ in range(self._size - 2):
                previous_node = previous_node.next

        # if only one node
        if self._head == self._tail:
            self._head = None

        # take value
        value = self._tail.data

        # remove last node
        self._tail = previous_node

        # fix next pointer
        if self._tail:
            self._tail.next = None

        # decrease size
        self._size -= 1

        return value

    def insert(self, index, value):
        # check index valid or not
        if index < 0 or index > self._size:
            raise(ValueError('Index out of bounds'))

        previous_node = None
        next_node = self._head

        # move to position
        for _ in range(index):
            previous_node = next_node
            next_node = next_node.next

        # create node
        new_node = ListNode(value, next_node)

        # if first position
        if previous_node is None:
            self._head = new_node
        else:
            previous_node.next = new_node
        
        # if insert at end
        if previous_node == self._tail:
            self._tail = new_node

        # increase size
        self._size += 1

    def remove(self, index):
        # check index
        if index < 0 or index >= self._size:
            raise ValueError('Index out of bounds')

        # if remove first
        if index == 0:
            value = self._head.data
            self._head = self._head.next

            # if list empty now
            if self._head is None:
                self._tail = None
        else:
            # go before index
            previous = self._head
            for _ in range(index - 1):
                previous = previous.next

            current = previous.next
            value = current.data

            # remove node
            previous.next = current.next

            # if last removed
            if current == self._tail:
                self._tail = previous

        # decrease size
        self._size -= 1

        return value
    

#this code make a linked list where we
#  can add, remove and insert values
#it works by connecting nodes together 
# and changing links when we update list