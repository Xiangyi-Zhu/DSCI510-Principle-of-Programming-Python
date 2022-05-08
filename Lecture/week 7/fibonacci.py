# Fibonacci series module

def fib(n):    # Print Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print (b, end = ' ')  # Note!
        a, b = b, a+b
    print()                   # Why?

def fib2(n):   # Return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result