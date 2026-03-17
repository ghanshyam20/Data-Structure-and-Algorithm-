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


def find_min(root):
    if root is None:
        return None

    if root.left is None:
        return root.value

    return find_min(root.left)


# -------- MAIN PART --------

root = None
values = [13, 7, 3, 8, 15, 14, 19, 18]

for v in values:
    root = insert(root, v)

print("Lowest value in BST:", find_min(root))
