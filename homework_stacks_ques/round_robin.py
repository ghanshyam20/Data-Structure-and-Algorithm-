#i haev  use list as queue 

tasks = [("A", 3), ("B", 6), ("C", 1)]

finished = []   #  thsi is to store completed task names

# thsi  loop go till  queue becomes empty
while len(tasks) > 0:

    #  thsi will take first task from queue
    current = tasks.pop(0)

    name = current[0]          
    time_needed = current[1]   

    # give 2 time units
    time_needed = time_needed - 2

    #  thsi will check if task is finished or not 
    if time_needed > 0:
        # not finished → put back in queue
        tasks.append((name, time_needed))
    else:
        # finished and apend thename as save
        finished.append(name)

# print result
print(finished)