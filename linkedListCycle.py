# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        
        if head == None:
            return False
        
        
        count = 0
        
        while count <= 10001:   # already know number of nodes <= 10000
            count += 1
            
            head = head.next

            if head == None:
                return False
            
            
        return True
                
            
