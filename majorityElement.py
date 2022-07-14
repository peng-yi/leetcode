class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        counts = {}
        
        for num in nums:
            if num not in counts: counts[num] = 1
            else:   counts[num] += 1
        
        maj = max(counts.values())
        for key in counts.keys():
            if counts[key] == maj:  return key
