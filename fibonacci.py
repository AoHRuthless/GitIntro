# The Fibonacci numbers, form what is called the Fibonacci sequence, such that 
# each number is the sum of the two preceding ones, starting from 0 and 1.

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def fast_fib(n):
    memo = [0, 1]
    
    if n < 2:
        return memo[n]
    
    for x in range(2, n + 1):
        memo.append(memo[x-2] + memo[x-1])
    
    return memo[-1]