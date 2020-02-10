def max_sub_array(nums):
        dp = [[0 for j in range(len(nums))] for i in range(len(nums))]
        max_sum = -float('inf')
        
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if j == 0:
                    result = nums[j]
                elif i == 0:
                    
                    result = nums[j] + dp[i][j-1]
                else:
                    result = max(nums[j] + dp[i][j-1], dp[i-1][j])
                
                dp[i][j] = result
                
                if result > max_sum:
                    max_sum = result
                
        return max_sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_sub_array(nums))