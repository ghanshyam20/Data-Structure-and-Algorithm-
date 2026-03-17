def reverse_first_three(queue):

    stack = []   # i will sue  this to   reverse

    # thsi will  take first 3 elements from queue
    i = 0
    while i < 3:
        if len(queue) > 0:
            x = queue.pop(0)   #  it will remove from front
            stack.append(x)    # it wil  put in stack
        i = i + 1

    #thsi will  put back from stack 
    while len(stack) > 0:
        queue.insert(0, stack.pop())   # it iwll add to front

    return queue


#thsi is for testinfg 
q = [1, 2, 3, 4, 5]

print("Before:", q)

q = reverse_first_three(q)

print("After:", q)