class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        
        return 1162261467 % n == 0  # largest 3 power under 2^31
        
