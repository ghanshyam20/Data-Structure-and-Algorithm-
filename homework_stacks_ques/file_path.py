#  thsi is for input path
path = "/home//user/.././docs"

# split by "/" to get parts
parts = path.split("/")

stack = []   #  i have use stack to store folders

#  this will go through each part
for part in parts:

    # ignore empty and "."
    if part == "" or part == ".":
        continue

    # if ".." go back
    elif part == "..":
        if len(stack) > 0:
            stack.pop()   #  this will move to go one folder back

    else:
        #  thiw iwll push to normal folder  abd  add to stack
        stack.append(part)

# it will  build final path
result = "/" + "/".join(stack)

print(result)