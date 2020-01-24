# Recursive non-dp solution to 0-1 Knapsack
def knapsack_recursive(weights, values, capacity):
    """
    Method determines the maximum value resulting from a combination of items
    in the knapsack.

    Parameters:
        weights (int): List of item weights.
        values (int): List of item values.
        capacity (int): Maximum weight of knapsack
    
    Returns:
        value (int): Max value resulting from combinations of
            items constrained by capacity.
    """
    item = len(weights) -1
    return _knapsack_recursive(weights, values, capacity, item)

def _knapsack_recursive(weights, values, capacity, item):
    print(f'ks({capacity}, {item})')
    # Base Case: No more items
    if item < 0 or capacity == 0:
        return 0
    
    # Base Case: item's weight is greater than availible capacity
    if weights[item] > capacity:
        return _knapsack_recursive(weights, values, capacity, item - 1)

    # Max compare the results of taking or skipping the item
    take = values[item] + _knapsack_recursive(weights, values, capacity - weights[item], item - 1)
    skip = _knapsack_recursive(weights, values, capacity, item - 1)
    #print(f'Item: {item} | Take: {take} vs. Skip: {skip}')
    return max(take,skip)

def knapsack_recursive_2(weights, values, capacity):
    """
    Method determines the maximum value and combination of items.

    Parameters:
        weights (int): List of item weights.
        values (int): List of item values.
        capacity (int): Maximum weight of knapsack
    
    Returns:
        value (int): Max value resulting from combinations of
            items constrained by capacity.
        in_ks (int): Index values of items in knapsack
    """
    item = len(weights) - 1
    in_ks = []
    max_val = _knapsack_recursive_2(weights, values, capacity, item, in_ks)

    return in_ks, max_val

def _knapsack_recursive_2(weights, values, capacity, item, in_ks):
    if item < 0 or capacity == 0:
        return 0

    if weights[item] > capacity:
        return _knapsack_recursive_2(weights, values, capacity, item - 1, in_ks)
    
    take = values[item] + _knapsack_recursive_2(weights, values, capacity - weights[item], item -1, in_ks)
    skip = _knapsack_recursive_2(weights, values, capacity, item - 1, in_ks)

    if take > skip:
        in_ks.append(item)
        return take
    else:
        in_ks.pop()
        return skip




def knapsack_bottom_up(weights, values, capacity):
    result = []
    for j in range(len(weights)):
        result_row = []
        for i in range(capacity + 1):
            if j == 0 and weights[j] > i:
                result_row.append(0)
            elif j == 0:
                result_row.append(values[j])
            elif weights[j] > i:
                result_row.append(result[j-1][i])
            else:
                take = values[j] + result[j-1][i-weights[j]]
                skip = result[j-1][i]
                result_row.append(max(take, skip))
        result.append(result_row)

    return result

if __name__ == "__main__":
    capacity = 8
    #weights = [1, 2, 4, 2, 5]
    #values = [5, 3, 5, 3, 2]
    weights = [2,2,4,5]
    values = [2,4,6,9]
    #print(knapsack_recursive(weights, values, len(weights)-1, capacity ))     
    print(knapsack_recursive(weights, values, capacity))     
    print(knapsack_bottom_up(weights, values, capacity))
    print(knapsack_recursive_2(weights, values, capacity))     
