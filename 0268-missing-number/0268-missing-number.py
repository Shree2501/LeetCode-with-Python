class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        a = 0
        if n == 1:
            if nums[a] == 1:
                return 0
            return 1
        for i in range(1,n+1):
            if i not in nums:
                return i
        return 0
            
            
            
        