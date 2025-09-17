# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        ls = []
        current = head
        while current:
            ls.append(current)
            current = current.next
        
        n = len(ls)
        
        
        node1 = ls[k-1]
        node2 = ls[n-k]
        
        node1.val, node2.val = node2.val, node1.val
        
        return head

