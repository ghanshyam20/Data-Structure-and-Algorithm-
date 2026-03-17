class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data   # store data
        self._parent = parent_node   # parent node
        self._left_child = left_child   # left child
        self._right_child = right_child   # right child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None   # tree is empty in start

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        # add new value in tree (BST rule)
        current_node = self._root_node
        parent_node = None

        # go down tree to find place
        while current_node is not None:
            parent_node = current_node

            if data <= current_node.data:
                current_node = current_node._left_child   # go left
            else:
                current_node = current_node._right_child  # go right

        new_node = Node(data, parent_node=parent_node)

        # if tree empty
        if parent_node is None:
            if self._root_node is None:
                self._root_node = new_node
            else:
                raise(ValueError)

        # attach left or right
        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node

    def _find(self, data):
        # find value in tree
        current = self._root_node

        while current is not None:

            if current.data == data:
                return current   # found

            elif current.data > data:
                current = current._left_child   # go left

            else:
                current = current._right_child  # go right

        return None   # not found

    def find_minimum(self):
        # minimum is most left node
        current = self._root_node

        if current is None:
            return None   # tree empty

        # go left until no more
        while current._left_child is not None:
            current = current._left_child

        return current

    def find_maximum(self):
        # maximum is most right node
        current = self._root_node

        if current is None:
            return None   # tree empty

        # go right until no more
        while current._right_child is not None:
            current = current._right_child

        return current