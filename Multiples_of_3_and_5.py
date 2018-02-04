"""
Problem Statement: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
def multiples(limit = 1000):
    """
    Returns the multiples of 3 and 5
    """
    number = 1
    multi = []
    while(number <= 1000):
        if(number%3 == 0 and number%5 == 0):
            multi.append(number)
        if (number < 0):
            break
    return multi


def sum_of_multiples(limit = 1000):
    """
    Returns the sum of the multiples below the limit
    """
    return sum(multiples(limit))


print(sum_of_multiples())
