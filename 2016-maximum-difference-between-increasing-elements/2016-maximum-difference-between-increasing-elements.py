class Solution(object):
    def maximumDifference(self, nums):
        min_index = float('inf')
        max_diff = 0
        for i in range(0,len(nums)):
            min_index = min(min_index, nums[i])
            max_diff = max(max_diff, nums[i]-min_index)
        if max_diff == 0:
            return -1
        return max_diff
