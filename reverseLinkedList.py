# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        nodes = [head]
                
        while head.next != None:
            head = head.next
            nodes.append(head)
            #print(nodes)
        
        newnodes = []
        for i in range(len(nodes)):
            newnodes.append(nodes[len(nodes)-1-i])
        #newnodes = nodes.reverse()
        #print(newnodes)
            
        for i in range(len(nodes)-1):
            newnodes[i].next = newnodes[i+1]
            
        newnodes[len(nodes)-1].next = None
        
        return newnodes[0]
        
        
