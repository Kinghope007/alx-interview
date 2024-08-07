#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to meet with the fewest number of coins.
        
    Returns:
        int: The fewest number of coins needed to meet the total amount.
             If the total is 0 or less, return 0.
             If the total cannot be met by any number of coins you have, return -1.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
