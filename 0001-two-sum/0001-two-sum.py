class Solution(object):
    def twoSum(self, nums, target):
        res = []
        n = len(nums)
        for i in range(0,n-1):
            sum = 0
            for j in range(i+1,n):
                sum = nums[i] + nums[j]
                if(sum == target):
                    return i,j
        