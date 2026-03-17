# these are stack of actions 
stack = ["open", "edit", "save", "close"]

n = 2   #  thsi is number of actions to undo

undone = []   #  thsi is to store undone actions

# run loop n times
for i in range(n):

    # check if stack is empty before popping
    if len(stack) == 0:
        break   # stop if nothing left

    # remove last action
    action = stack.pop()

    # store undone action
    undone.append(action)

# print results
print("undone:", undone)
print("left in stack:", stack)