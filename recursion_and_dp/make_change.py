# Given a list of coin values and a target, find the least number of coins to make change.

# Brute force recursive solution:
def make_change_1(coins, target):
    print(f'make_change_1({coins}, {target})')
    if target == 0:
        return [0 for _ in coins]

    min_coins = [float('inf') for _ in coins]
    for coin in coins:
        if coin == target:
            return min_coins[i] = 1
        elif coin < target:
            print(f'1 + make_change_1({coins}, {target} - {coin})')
            return 1 + make_change_1(coins, target - coin)




if __name__ == "__main__":
    coins = [1, 2, 3] 
    target = 5

    print(make_change_1(coins, target))