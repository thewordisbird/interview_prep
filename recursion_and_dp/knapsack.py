# Recursive non-dp solution to 0-1 Knapsack

def knapsack_recursive(weights, values, item, capacity):
    if item < 0 or capacity == 0:
        return 0
    elif weights[item] > capacity:
        return knapsack_recursive(weights, values, item-1, capacity)
    else:
        return max(knapsack_recursive(weights, values, item-1, capacity), \
            values[item] + knapsack_recursive(weights, values, item - 1, capacity - weights[item]))


if __name__ == "__main__":
    capacity = 5
    weights = [1, 2, 4, 2, 5]
    values = [5, 3, 5, 3, 2]
    print(knapsack_recursive(weights, values, len(weights)-1, capacity ))     