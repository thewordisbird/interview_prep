def ms_naive(nums):
    print(f'ms_naive({nums})')
    if len(nums) > 0:
        include = [nums[0]] + ms_naive([x for x in nums[1:] if x > nums[0]])
        exclude = ms_naive(nums[1:])
        #print(f'compoaring: {include} | {exclude}')
        if sum(include) > sum(exclude):
            return include
        else:
            return exclude
    else:
        return []

def ms_top_down(nums, i=0, cache = {}):
    print(f'ms_top_down({nums}, {i}, cache)')
    if i < len(nums):
        if i in cache:
            #print('Using Cache')
            return cache[i]
        
        include = [nums[i]] + ms_top_down(nums, next_i(nums, i, True), cache)
        exclude = ms_top_down(nums, next_i(nums, i, False), cache)
        #print(f'compoaring: {include} | {exclude}')
        if sum(include) > sum(exclude):
            print(f'cacheing {i}, {include}')
            cache[i] = include
            return include
        else:
            print(f'cacheing {i}, {exclude}')
            cache[i] = exclude
            return exclude
    else:
        return []

def next_i(array, index, include=True):
    if index >= len(array):
        return len(array)
    val = array[index]
    
    while index < len(array):
        #print(f'{array[index]} > {val}')
        if array[index] > val and include:
            #print(f'returning {index}')
            return index
        else:
            include = True
        index += 1


    return len(array)

    


if __name__ == "__main__":
    #nums = [3, 14, 1, 5, 13, 26, 53, 59]
    #nums = [14, 1, 5, 10, 26]
    nums = [10,15,4,5,11,14,31,25,31,23,25,31,50]
    print("Running Naive")
    print(ms_naive(nums))
    nums = [10,15,4,5,11,14,31,25,31,23,25,31,50]
    print("Running Top-Down")
    print(ms_top_down(nums))