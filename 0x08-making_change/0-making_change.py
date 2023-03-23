#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """this functions determines the fewest number of coins needed to meet
    a given amount total - using coins of different values"""
    if total <= 0:
        return 0
    coins = sorted(coins)
    coinTotal = 0
    minCoins = 0
    for coin in coins:
        res = (total - coinTotal)//coin
        curTotal += res*coin
        minCoins += res
        if coinTotal == total:
            return minCoins
    return -1
