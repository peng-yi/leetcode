# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        m=1
        head = headA
        while head.next != None:
            head = head.next
            m += 1
        n=1
        head = headB
        while head.next != None:
            head = head.next
            n += 1
        
        
        if m > n:
            for i in range(m-n):
                headA = headA.next
        if m < n:
            for i in range(n-m):
                headB = headB.next
        
        
        for i in range(min(m,n)):
            if (headA == headB): return headA
            else:
                headA = headA.next
                headB = headB.next
        
        return None
            
