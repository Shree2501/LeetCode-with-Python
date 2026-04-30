class Solution(object):
    def twoSum(self, nums, target):
        freq = {}
        n = len(nums)
        for i in range(n):
            val = target - nums[i]
            if val in freq:
                return freq[val],i
            freq[nums[i]] = i