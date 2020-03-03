def lms(nums):
    cache = {}

    for i, num in enumerate(nums):
        if num not in cache:
            _lms(nums[i+1:], num, cache)
    
    return cache

def _lms(nums, mod, cache):
    if len(nums) > 0:
        if mod in cache:
            return cache[mod]
        else:
            cache[mod] = [mod]
        
        subset = []
        for num in nums:
            if num%mod == 0:
                subset.append(num)
        print(mod, nums)
        
        result=[]
        for i, n in enumerate(subset):
            mod_list = _lms(subset[i+1:], n, cache)
            if len(mod_list) > len(result):
                result.append(mod_list)
        cache[mod] = cache[mod] + result

        return cache[mod]
    return []

if __name__ == "__main__":
    nums = [3, 5, 10, 15, 20, 21]

    print(lms(nums))