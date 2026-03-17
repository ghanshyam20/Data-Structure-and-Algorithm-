# this code is from option chapter 5 




class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data   # store data inside node
        self._parent = parent_node   # parent node link
        self._left_child = left_child   # left side
        self._right_child = right_child   # right side

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None   # tree is empty in begining

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        # insert new value in tree using bst rule
        current_node = self._root_node
        parent_node = None

        # go down tree to find correct place
        while current_node:
            parent_node = current_node

            if data <= current_node.data:
                current_node = current_node._left_child   # go left side
            else:
                current_node = current_node._right_child  # go right side

        new_node = Node(data, parent_node=parent_node)

        # if tree is empty
        if parent_node is None:
            self._root_node = new_node
        else:
            # attach node to parent
            if new_node.data < parent_node.data:
                parent_node._left_child = new_node
            else:
                parent_node._right_child = new_node

    def _find(self, data):
        # find node by value
        current = self._root_node

        while current:

            if current.data == data:
                return current   # found node

            elif current.data > data:
                current = current._left_child   # go left

            else:
                current = current._right_child  # go right

        return None   # not found

    def delete_node(self, data):
        # delete node from tree by value

        node = self._find(data)   # first find node

        if node is None:
            return   # nothing found so return

        # case 1: node has no child (leaf)
        if node._left_child is None and node._right_child is None:

            if node._parent is None:
                self._root_node = None   # only root exist
            else:
                if node._parent._left_child == node:
                    node._parent._left_child = None
                else:
                    node._parent._right_child = None

        # case 2: node has only one child
        elif node._left_child is None or node._right_child is None:

            if node._left_child is not None:
                child = node._left_child
            else:
                child = node._right_child

            if node._parent is None:
                self._root_node = child
                child._parent = None
            else:
                if node._parent._left_child == node:
                    node._parent._left_child = child
                else:
                    node._parent._right_child = child

                child._parent = node._parent

        # case 3: node has two child
        else:
            # find smallest in right side
            temp = node._right_child

            while temp._left_child is not None:
                temp = temp._left_child

            # copy value
            node.data = temp.data

            # now remove that temp node
            if temp._right_child is not None:
                child = temp._right_child
            else:
                child = None

            if temp._parent._left_child == temp:
                temp._parent._left_child = child
            else:
                temp._parent._right_child = child

            if child is not None:
                child._parent = temp._parent