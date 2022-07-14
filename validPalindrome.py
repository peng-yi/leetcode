class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        news = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                news += i
        
        news = news.lower()
        
        return news == news[::-1]
