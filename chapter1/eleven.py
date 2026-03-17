def combine_lists(list1, list2):
    result = []
    
    i = 0
    j = 0

    # compare both lists
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i = i + 1
        else:
            result.append(list2[j])
            j = j + 1

    # add remaining items from list1
    while i < len(list1):
        result.append(list1[i])
        i = i + 1

    # add remaining items from list2
    while j < len(list2):
        result.append(list2[j])
        j = j + 1

    return result


# this function taskes tow sorted lists and combines them into one sorted list and 
# it compares elements one by one addds the smmler on to the result.