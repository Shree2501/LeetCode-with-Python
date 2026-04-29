class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        i = 0
        count = 0
        max_count = 0
        while(i<n):
            if nums[i] == 0:
                count = 0
                i+=1
            else:
                count += 1
                i+=1
            max_count = max(max_count,count)
        return max_count
        