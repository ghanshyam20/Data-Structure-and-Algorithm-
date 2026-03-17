class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None   # tree start empty

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        # insert new value in tree
        current_node = self._root_node
        parent_node = None

        # go down until place found
        while current_node is not None:
            parent_node = current_node

            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        new_node = Node(data, parent_node=parent_node)

        # if no parent means empty tree
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
                return current

            # go left
            if data < current.data:
                current = current._left_child
            else:
                # go right
                current = current._right_child

        return None

    def _detach_node(self, node):
        # remove node from tree, only max 1 child allowed

        if node is None:
            return   # nothing to do

        # if node has 2 child then not allowed
        if node._left_child is not None and node._right_child is not None:
            raise ValueError

        # find child if exist
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

        # check node is left or right side
        if parent._left_child == node:
            parent._left_child = child
        else:
            parent._right_child = child

        # update child parent link
        if child is not None:
            child._parent = parent



