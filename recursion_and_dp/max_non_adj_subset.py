def max_sum_recursive(nums):
    index = len(nums) - 1
    return _max_sum_recursive(nums, index)

def _max_sum_recursive(nums, index):
    print(f'_max_sum_recursive({nums}, {index})')
    if index < 0:
        return 0

    include = nums[index] + _max_sum_recursive(nums, index - 2)
    exclude = _max_sum_recursive(nums, index - 1)
    return max(include, exclude)


def max_sum_top_down(nums):
    index = len(nums) - 1
    cache = {}
    return _max_sum_top_down(nums, index, cache)

def _max_sum_top_down(nums, index, cache):
    print(f'_max_sum_top_down({nums}, {index}, {cache})')
    if index < 0:
        result =  0
    elif index in cache:
        result = cache[index]
    else:
        include = nums[index] + _max_sum_top_down(nums, index - 2, cache)
        exclude = _max_sum_top_down(nums, index - 1, cache)
        result = max(include, exclude)
        cache[index] = result
    return result
    
def max_sum_bottom_up(nums):
    
    

if __name__ == "__main__":
    nums = [75, 105, 120, 75, 90, 135, 13, 24, 69, 12]
    #nums = [1, 15, 3]
    print(max_sum_recursive(nums))

    print(max_sum_top_down(nums))