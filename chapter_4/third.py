class StackBasedQueue():
    def __init__(self):
        # using two stack for make queue
        self._InboundStack = Stack()    # new items come here
        self._OutboundStack = Stack()   # items go out from here
        self._size = 0                  # total elements

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack]
        values.extend([c for c in self._OutboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        # add item to queue (put in inbound stack)
        self._InboundStack.push(data)
        self._size = self._size + 1

    def dequeue(self):
        # remove item from queue

        if self._size == 0:
            return None   # nothing in queue

        # if outbound empty then move all from inbound
        if len(self._OutboundStack) == 0:
            while len(self._InboundStack) != 0:
                temp = self._InboundStack.pop()
                self._OutboundStack.push(temp)

        self._size = self._size - 1
        return self._OutboundStack.pop()   # return removed item