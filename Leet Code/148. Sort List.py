# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        if head.next is None:
            return head

        ls = []
        current = head
        while current:
            ls.append(current.val)
            current = current.next

        ls.sort()

        dummy = ListNode(0)
        new = dummy
        for val in ls:
            new.next = ListNode(val)
            new = new.next

        return dummy.next