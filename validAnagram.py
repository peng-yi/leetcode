class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list((s))
        t = list((t))
        s = sorted(s)
        t = sorted(t)
        #print(s)
        #print(t)
        
        return s == t
        
