

def perm(nums):
    result = []
    if len(nums) == 1:
        result.append(nums[0])
    else:
        for i,n in enumerate(nums):
            result = [n] + perm(nums[:i] + nums[i+1:])
    
    return result

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(perm(nums))