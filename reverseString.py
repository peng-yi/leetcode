class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        l = len(s)
        n = l //2
        
        for i in range(n):
            c = s[i]
            s[i] = s[l-1-i]
            s[l-1-i] = c
            
        return s
