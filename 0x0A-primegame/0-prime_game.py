#!/usr/bin/python3
"""
This module contains the prime game as stated in the README.md file.
"""


def primeNumbers(n):
    """this function returns prime numbers between 1 and n
    """
    primeNums = []
    sort = [True] * (n + 1)
    for p in range(2, n + 1):
        if sort[p]:
            primeNums.append(p)
            for i in range(p, n + 1, p):
                sort[i] = False
    return primeNums


def isWinner(x, nums):
    """this functions determines the winner of the game"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for n in range(x):
        primeNums = primeNumbers(nums[n])
        if len(primeNums) % 2 != 0:
            Maria += 1
        else:
            Ben += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
