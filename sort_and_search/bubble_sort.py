def bubble_sort(nums):
   
    for pass_num in range(len(nums) - 1, 0, -1):
        for i in range(pass_num):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                

if __name__== "__main__":
    nums = [1,5,2,7,4,9,3]
    bubble_sort(nums)
    print(nums)
