#!/usr/bin/python3
def fibonacci_sequence(n):
    fib_num = [0, 1]
    while len(fib_num) < n:
        next_num = fib_num[-1] + fib_num[-2]
        fib_num.append(next_num)
    return fib_num

