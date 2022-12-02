# Python program to demonstrate Basic Euclidean Algorithm
from math import *

#Function to perform gcd of num1 and num2
def euclid_algo(x, y, verbose=True):
    if x < y:  # We want x >= y
        return euclid_algo(y, x, verbose)
    print()
    while y != 0:
        if verbose: print('%s = %s * %s + %s' % (x, floor(x / y), y, x % y))
        (x, y) = (y, x % y)

    if verbose: print('gcd(', num1, ',', num2, ') = %s' % x)
    return x


print("""\n=== GCD: Using Euclidean Algorithm ===\n""")
try:
    num1 = int(input("Input first number: "))
    num2 = int(input("Input second number: "))
    euclid_algo(num1, num2)
except:
    print("Invalid Input, try again...")



