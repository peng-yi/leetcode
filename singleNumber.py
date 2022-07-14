class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        
        if length==1: return nums[0]
        
        a = [0] * 60001
        for i in range(length):
            a[nums[i]+30000] += 1
        
        return a.index(1)-30000
            
