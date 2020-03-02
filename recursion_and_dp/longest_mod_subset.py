def longest_mod_subset(nums, cache={}):
    if len(nums) > 1:

        for i, num in enumerate(nums):
            if num in cache:
                return caceh[num]
            result = []
            subset = []

            for j in range(i+1, len(nums)):
                if nums[j] % num == 0:
                    subset.append(nums[j])
            
            # need max for recursions
            valid_subset = [num]
            lms = max(longest_mod_subset()) 
            lms = longest_mod_subset(subset, cache)

            if num in cache and lms > cache[num] or num not in cache:
                cache[num] = lms

        return subset
    else:
        return nums[0]
    
