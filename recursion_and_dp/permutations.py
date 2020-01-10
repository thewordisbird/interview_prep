

def permutations(nums, perm=[], perms=[]):
    # Base case: An empty list is passed in. Add the perm list
    # to the perms list. 
    if len(nums) == 0:
        # In order to avoid appending the list by refrence, we need to append list[:].
        if perm:
            perms.append(perm[:])
    
    for i,n in enumerate(nums):
        perm.append(n)
        permutations(nums[:i] + nums[i+1:], perm, perms)
        # Backtrack by removing the last item added to perm
        perm.pop()
    
    return perms

if __name__ == "__main__":
    nums = [1, 2, 3]
    #print(permutations(nums))

    nums = [1,2]
    print(permutations(nums))