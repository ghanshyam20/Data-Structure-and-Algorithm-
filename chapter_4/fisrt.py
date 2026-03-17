class Node:
    def __init__(self, data=None, next=None):
        self.data = data      # store value
        self.next = next      # point to next node

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None      # top of stack
        self._size = 0        # how many elements

    def __len__(self):
        return self._size

    def peek(self):
        # just see top element, not removing
        if self._top:
            return self._top.data
        return None

    def push(self, data):
        # add new item on top
        new_node = Node(data)     # create node
        new_node.next = self._top # link to old top
        self._top = new_node      # update top
        self._size += 1           # increase size

    def pop(self):
        # remove top element
        if self._top is None:
            return None           # nothing to remove

        value = self._top.data    # take value
        self._top = self._top.next  # move top down
        self._size -= 1           # decrease size
        return value

    def __repr__(self):
        current = self._top
        values = []

        # loop through stack
        while current is not None:
            values.append(current.data)
            current = current.next

        # make string list (no quotes)
        val_str = "["
        for i in range(len(values)):
            val_str += str(values[i])
            if i != len(values) - 1:
                val_str += ", "
        val_str += "]"

        # check plural or not
        if self._size == 1:
            text = "element"
        else:
            text = "elements"

        return f'<Stack ({self._size} {text}): {val_str}>'
    

## simple stack using linked list, push add on top and pop remove
#  from top, size also update