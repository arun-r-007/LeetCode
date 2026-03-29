# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return head

        ls = []
        current = head
        while current is not None:
            ls.append(current.val)
            current = current.next

        mid = 0
        n = len(ls)
        if n % 2 != 0:
            mid = n // 2
        else :
            mid = (n / 2)

        current = head
        
        for i in range (mid):
            current = current.next
        
        return current