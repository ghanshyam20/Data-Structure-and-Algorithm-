#  this stack is just a list
stack = [5, 2, 9, 1, 7]

# first check if stack is empty
if len(stack) == 0:
    print("stack is empty")
else:
    # find smallest number using built-in function
    minimum = min(stack)

    # print result
    print(minimum)