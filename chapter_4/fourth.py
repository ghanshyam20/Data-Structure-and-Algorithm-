class Queue:
    def __init__(self):
        # make empty queue first
        self._head = None    # front side
        self._tail = None    # back side
        self._size = 0       # total items

    def enqueue(self, data):
        # add new item in left side
        new_node = ListNode(data)

        if self._head is None:
            # if empty then both same
            self._head = new_node
            self._tail = new_node
        else:
            # link new node in front
            new_node.next = self._head
            self._head = new_node

        self._size = self._size + 1

    def dequeue(self):
        # remove item from right side

        if self._tail is None:
            return None   # nothing to remove

        value = self._tail.data   # take value

        if self._head == self._tail:
            # only one element
            self._head = None
            self._tail = None
        else:
            current = self._head

            # go until one before tail
            while current.next != self._tail:
                current = current.next

            current.next = None
            self._tail = current   # update tail

        self._size = self._size - 1
        return value

    def __repr__(self):
        current = self._head
        values = []

        # go all nodes and store
        while current is not None:
            values.append(current.data)
            current = current.next

        # make string list (simple way)
        val_str = "["
        for i in range(len(values)):
            val_str += str(values[i])
            if i != len(values) - 1:
                val_str += ", "
        val_str += "]"

        # check plural word
        if self._size == 1:
            text = "element"
        else:
            text = "elements"

        return f'<Queue ({self._size} {text}): {val_str}>'
    

