
def get_pairs(numbers):
    even_q = Queue()   # queue for even numbers
    odd_q = Queue()    # queue for odd numbers
    result = []        # store pairs here

    # go all numbers one by one
    for num in numbers:

        # check even number
        if num % 2 == 0:

            # if odd already waiting then make pair
            if odd_q._size != 0:
                odd = odd_q.dequeue()
                result.append((num, odd))   # even first then odd
            else:
                even_q.enqueue(num)   # store even

        else:
            # number is odd

            # if even already waiting then make pair
            if even_q._size != 0:
                even = even_q.dequeue()
                result.append((even, num))
            else:
                odd_q.enqueue(num)   # store odd

    return result