class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        firstocc = [-1]*26
        counts = [0]*26
        
        for i,c in enumerate(s):
            counts[ord(c)-97] += 1
            if firstocc[ord(c)-97] < 0:
                firstocc[ord(c)-97] = i
        #print(counts)
        #print(firstocc)
        
        first = 100001
        found = 0
        for i in range(26):
            if counts[i] == 1:
                found = 1
                if firstocc[i] < first:
                    first = firstocc[i]
        if found:
            return first
        else:
            return -1
            
            
