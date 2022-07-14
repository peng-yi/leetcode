class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = [0]* (len(nums)+1)
        for i in nums:
            counts[i] += 1
        
        return counts.index(0)
