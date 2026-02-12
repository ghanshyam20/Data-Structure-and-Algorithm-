class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):

    # If tree empty OR reached empty spot
    if root is None:
        return Node(value)

    # If value smaller → go left
    if value < root.value:
        root.left = insert(root.left, value)

    # If value larger → go right
    elif value > root.value:
        root.right = insert(root.right, value)

    # Return unchanged root
    return root
