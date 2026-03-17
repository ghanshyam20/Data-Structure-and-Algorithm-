def check_balance(text):
    stack = Stack()   # create stack
    count = 0         # count pairs

    # pairs for matching
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # loop all characters
    for i in range(len(text)):
        ch = text[i]

        # if opening bracket then push
        if ch == '(' or ch == '[' or ch == '{':
            stack.push(ch)

        # if closing bracket then check
        elif ch == ')' or ch == ']' or ch == '}':
            if len(stack) == 0:
                # no opening but got closing
                return "Match error at position " + str(i)

            top = stack.pop()  # take last opening

            # if not match then error
            if pairs[ch] != top:
                return "Match error at position " + str(i)

            count = count + 1  # one pair done

    # after loop still something left means error
    if len(stack) != 0:
        return "Match error at position " + str(len(text) - 1)

    # all good
    return "Ok - " + str(count)
