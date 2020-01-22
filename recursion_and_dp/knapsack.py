# Recursive non-dp solution to 0-1 Knapsack

def knapsack_recursive(weights, values, item, capacity):
    if item < 0 or capacity < 1:
        return 0
    elif weights[item] > capacity:
        return 0
    else:
        return max(knapsack_recursive(weights, values, item-1, capacity), \
            values[item] + knapsack_recursive(weights, values, item - 1, capacity - weights[item]))

def knapsack_recursive_2(weights, values, capacity):
    if capacity < 1 or weights == []:  
        return 0
    elif weights[0] > capacity:
        return 0
    
    else:
        max_val = max(values[0] + knapsack_recursive_2(weights[1:], values[1:], capacity - weights[0]), knapsack_recursive_2(weights[1:], values[1:], capacity))

    return max_val

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
    capacity = 5
    #weights = [1, 2, 4, 2, 5]
    #values = [5, 3, 5, 3, 2]
    weights = [5,3,4,2]
    values = [60,50,70,30]
    #print(knapsack_recursive(weights, values, len(weights)-1, capacity ))     
    #print(knapsack_recursive_2(weights, values, capacity ))     
    ks = knapsack_bottom_up(weights, values, capacity)
    for r in ks:
        print(r)