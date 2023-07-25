#!/usr/bin/python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    fib_num = [0, 1]
    while len(fib_num) < n:
        next_num = fib_num[-1] + fib_num[-2]
        fib_num.append(next_num)
    return fib_num[:n]

