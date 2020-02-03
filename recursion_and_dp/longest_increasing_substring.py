# Given an array, find the longest strictly increasing substring
# Example:
# Given [8, 3, 5, 2, 4, 9, 7, 11]
# Return 4 ([3, 5, 9, 11], [3, 5, 7, 11], etc...)


def lis(nums):
    result = [0 for _ in range(len(nums))]
    for i in range(len(nums) - 1, -1, -1):
        # set to 1 for base case that number is larger than all numbers behind it
        choices = [(1, i)]
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                choices.append((result[j][0] + 1, i))
        result[i] = max(choices)

    return result

def print_substring(result, nums):    
    len_lis = max(result)[0]
    i = max(result)[1]
    arr_lis = [result[i][1]]

    while i < len(result):
            if len_lis - result[i][0] == 1:
                arr_lis.append(nums[result[i][1]])
                len_lis -= 1
            i += 1

    return arr_lis


def lis_td(nums):
    result = {}
    i = 0
    _lis_td(nums, i, result)
    return max(result.values())

def _lis_td(nums, i, result):
    #print(f'_lis_td({nums}, {i}, {result})')
    choices = []
    if i == len(nums) - 1:
        result[i] = 0
        return 0
    if i in result:
        return result[i]

    else:
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                choices.append(1 + _lis_td(nums, j, result))
            else:
                choices.append(_lis_td(nums, j, result)) 
        result[i] = max(choices)

        return max(choices)
    



if __name__ == "__main__":
    nums = [1, 8, 6, 3, 5, 2, 4, 9, 7, 11, 16, 13, 12, 14,]
    print(print_substring(lis(nums), nums))
    print(max(lis(nums))[0])
    print(lis_td(nums))