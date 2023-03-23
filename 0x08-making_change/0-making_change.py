#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """ This function returns the fewest number of coins
        from a coins list needed to meet a given total using
        coins of different values. 
    """
    if total <= 0:
       return 0
    coins = sorted(coins, reverse=True)
    coinTotal = 0;
    minCoins = 0;
    for c in coins:
        res = (total - coinTotal)
        coinTotal += res*c
        minCoins += res
        if coinTotal == total:
           return minCoins
    return -1
