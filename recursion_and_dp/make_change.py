# Given a list of coin values and a target, find the least number of coins to make change.

# Brute force recursive solution:
def make_change_1(coins, value):
    # Naive recursive solution
    print(f'make_change_1({coins}, {value})')
    if value == 0:
        return 0

    min_coins = float('inf')
    for coin in coins:
        if value - coin >= 0:
            min_coins = min(min_coins, 1 + make_change_1(coins, value - coin))
    return min_coins

def make_change_2(coins, value, cache={}):
    # Memoized recursive solution
    print(f'make_change_2({coins}, {value})')
    if value == 0:
        return 0
    
    if value in cache:
        return cache[value]

    min_coins = float('inf')
    for coin in coins:
        if value - coin >= 0:
            min_coins = min(min_coins, 1 + make_change_2(coins, value - coin))
    cache[value] = min_coins
    return min_coins

def make_change_3(coins, value):
    # Bottom up
    result = []
    for i in range(len(coins)):
        result_row = []
        for j in range(value + 1):
            if j == 0:
                result_row.append(0)
            elif coins[i] > j and i < 1:
                result_row.append(0)
            elif coins[i] > j: 
                result_row.append(result[i-1][j])
            elif coins[i] <= j and i == 0:
                result_row.append(1 + result[i][j-coins[i]])
            else:
                result_row.append(min(1 + result[i][j-coins[i]], result_row[i-1][j]))
        result.append(result_row)

    return result




if __name__ == "__main__":
    coins = [1, 2, 4, 7, 13] 
    value = 200

    print(make_change_3(coins, value))