class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data   # store value
        self._parent = parent_node   # parent link
        self._left_child = left_child   # left child
        self._right_child = right_child   # right child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None   # tree empty start

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        # add value in tree
        current_node = self._root_node
        parent_node = None

        # go down find place
        while current_node:
            parent_node = current_node

            if data <= current_node.data:
                current_node = current_node._left_child   # go left
            else:
                current_node = current_node._right_child  # go right

        new_node = Node(data, parent_node=parent_node)

        # if empty tree
        if parent_node is None:
            if self._root_node is None:
                self._root_node = new_node
            else:
                raise(ValueError)

        # attach node
        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node

    def _find(self, data):
        # search node in tree
        current = self._root_node

        while current:

            if current.data == data:
                return current   # found

            elif current.data > data:
                current = current._left_child   # go left

            else:
                current = current._right_child  # go right

        return None   # not found

    def _detach_node(self, node):
        # remove node from tree, only 0 or 1 child allowed

        if node is None:
            return   # nothing

        # if two child then error
        if node._left_child is not None and node._right_child is not None:
            raise ValueError

        # check child exist or not
        if node._left_child is not None:
            child = node._left_child
        else:
            child = node._right_child

        # if node is root
        if node._parent is None:
            self._root_node = child
            if child is not None:
                child._parent = None
            return

        parent = node._parent

        # check node is left or right
        if parent._left_child == node:
            parent._left_child = child
        else:
            parent._right_child = child

        # update child parent link
        if child is not None:
            child._parent = parent