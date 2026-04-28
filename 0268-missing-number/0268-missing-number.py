class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        freq_map = {}
        for i in range(0,n+1):
            freq_map[i] = 0
            if i in nums:
                freq_map[i] = 1
        for key,value in freq_map.items():
            if value == 0:
                return key    

                
            
            
            
        