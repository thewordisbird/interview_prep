def product_sum(arr, multiple=0):
    print(f'arr: {arr}, multiple: {multiple}')
    sum = 0
    for item in arr:        
        if type(item) == int:
            print(f'Multiplying {multiple + 1} * {item} = {sum + ((multiple + 1) * item)}')
            sum = sum + ((multiple + 1) * item)
        else:
            print(f'Recursing on {item}')
            sum = sum + ((multiple + 1) * product_sum(item, multiple + 1))
    print(f'returning {sum}')
    return sum

if __name__ == "__main__":
    arr1 = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    arr2 = [[[[[5]]]]]
    print(product_sum(arr1))
    print(product_sum(arr2))