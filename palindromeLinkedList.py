# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val       # value between 0-9
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        vals = ""
        vals += str(head.val)
        while head.next != None:
            head = head.next
            vals += str(head.val)
        
        return vals == vals[::-1]
        
