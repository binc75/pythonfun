#!/usr/bin/env python3

#
# Money change calculator
#

# Available coins list
coins = [5, 2, 1, 0.5, 0.2, 0.1, 0.05]

def coins_count(amount):
    '''Given an amount of money it divide it by the available coins change and give back a dictonary'''

    # Check if the amount is at least more that the smallest coin
    if amount >= min(coins):

        # Initialize local vars
        remaining = amount  # first assign the "remaining" to "amount", then decreased by the loop
        coins_counting = {} # initialize a dictionary to store the coins/count

        # Loop over the list of coins reverse sorted
        for coin in sorted(coins, reverse = True, key=float):

            # if the remaining amount is bigger than the coin
            if coin <= remaining:

                # Calculate 
                coin_count = remaining // coin # Floor division / Integer division

                # If for the current coin is usable (at least one coin), add the info to the dict
                if coin_count > 0:
                    coins_counting[coin] = int(coin_count)
                    remaining = round(remaining - (coin * coin_count), 2)

        return coins_counting

    else:
        return f'The given amount ({amount}) is less than smallest available coin ({min(coins)})'

# Main
result = coins_count(23.85)
print(result)
