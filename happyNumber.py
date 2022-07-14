class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = str(n)
        history = [n]
        
        while True:
            
            value = 0
            for c in n:
                value += int(c)**2
            n = str(value)
            
            if  n == '1': return True
            else:
                if n in history: return False
                history.append(n)
                
