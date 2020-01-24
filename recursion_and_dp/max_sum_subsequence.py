def max_sum_subsequence(nums):
    index = 0
    temp = []
    result = [-float('inf')]
    return _max_sum_subsequence(nums, index, temp, result)
    

def _max_sum_subsequence(nums, index, temp, result):
    print(f'_max_sum_subsequence({nums}, {index}, {temp}, {result})')
    if index < len(nums) - 1:
        if index == 0 or not temp or (temp and nums[index] > temp[-1]):
            temp.append(nums[index])
            result = _max_sum_subsequence(nums, index+1, temp, result)
            temp.pop()
        result = _max_sum_subsequence(nums, index+1, temp, result)

    else:
        print('Comparing lists')
        if sum(temp) > sum(result):
            result = temp[:]
    
    return result
    
    

if __name__ == "__main__":
    nums = [10, 70, 20, 30, 50, 11 ,30]
    print(max_sum_subsequence(nums))