import math

def hypotenuse(a, b):

    return math.sqrt(a**2 + b**2)

import math

def num_digits(n):

    n = int(n)  # ensure integer input
    if n == 0:
        return 1
    return len(str(abs(n)))

import math

def tip_amount(total, percent):

     return total * (percent / 100)
