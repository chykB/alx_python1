#!/usr/bin/python3
def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return True
            else:
                return False
