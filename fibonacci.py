# The Fibonacci numbers, form what is called the Fibonacci sequence, such that 
# each number is the sum of the two preceding ones, starting from 0 and 1.

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 1)