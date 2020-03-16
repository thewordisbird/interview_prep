def Binary_Search(nums, target):
    # nums must be sorted before starting
    start = 0
    end = len(nums) - 1
    mid = (start + end) // 2

    while start <= end:
        print(start, mid, end)
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2

    return False

if __name__ == "__main__":
    nums = [1,3,5,7,9,11]
    print(Binary_Search(nums,4))