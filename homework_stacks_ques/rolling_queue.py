queue = []   # this will store numbers,empty at first

while True:
    user_input = input("enter number,press enter to stop ")

    #  thsi will check empty input
    if user_input == "":
        break

    #  this iwll convert to int
    num = int(user_input)

    #  thsi will add to queue
    queue.append(num)

    # if more than 5 it will  remove from front
    if len(queue) > 5:
        queue.pop(0)

print("final queue:", queue)