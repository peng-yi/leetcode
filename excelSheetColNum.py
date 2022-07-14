class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        value = 0
        columnTitle = columnTitle[::-1]
        
        for i,c in enumerate(columnTitle):
            value += 26**i * (ord(c)-ord('A')+1)
            
        return value
