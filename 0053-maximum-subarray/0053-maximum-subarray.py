class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        maxSum = float("-inf")
        sum = 0
        if n == 1:
            return nums[0]
        for i in range(0,n):
            sum += nums[i]
            maxSum = max(maxSum, sum)
            if(sum < 0):
                sum = 0 
        return maxSum