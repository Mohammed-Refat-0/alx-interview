#!/usr/bin/python3

'''making change problem module'''


def makeChange(coins, total):
    '''determine the fewest number of coins
    needed to meet a given amount total, otherwise -1 if not possible
    '''
    if total <= 0:
        return 0

    rem = total
    count = 0
    index = 0
    sorted_coins = sorted(coins, reverse=True)

    while rem > 0:
        if index >= len(coins):
            return -1
        if rem - sorted_coins[index] >= 0:
            rem -= sorted_coins[index]
            count += 1
        else:
            index += 1
    return count
