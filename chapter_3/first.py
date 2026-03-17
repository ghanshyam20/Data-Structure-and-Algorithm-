class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
    def __init__(self):
        # head start as empty
        self._head = None

    def __repr__(self):
        # printing list values
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'

    def append(self, value):
        # making new node
        node = ListNode(value)

        # if list empty just put first
        if not self._head:
            self._head = node
        else:
            # go till last node
            current_node = self._head
            while current_node.next != None:
                current_node = current_node.next

            # connect new node
            current_node.next = node

    def pop(self):
        # if nothing inside
        if self._head is None:
            return None

        # if only one item
        if self._head.next is None:
            data = self._head.data
            self._head = None   # just remove it
            return data

        # more nodes case
        current_node = self._head

        # go second last
        while current_node.next.next is not None:
            current_node = current_node.next

        # take last value
        data = current_node.next.data

        # remove last node
        current_node.next = None

        return data