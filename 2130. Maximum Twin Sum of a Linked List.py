# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        if head.next.next is None:
            return (head.val + head.next.val)

        ls = []
        current = head
        while current is not None :
            ls.append(current.val)
            current = current.next

        n = len(ls)
        max1 = 0

        for i in range(n/2):
            k = ls[i] + ls[n-1-i]
            if max1 < k:
                max1 = k

        return max1