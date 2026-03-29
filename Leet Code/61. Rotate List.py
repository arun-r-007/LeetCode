# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if not head or not head.next or k == 0:
            return head
        
        n = 1
        current = head

        while current.next:
            current = current.next
            n += 1

        current.next = head

        k = k % n

        step = n - k

        current_tail = head

        for i in range(step - 1):
            current_tail = current_tail.next


        current_head = current_tail.next
        current_tail.next = None

        return current_head