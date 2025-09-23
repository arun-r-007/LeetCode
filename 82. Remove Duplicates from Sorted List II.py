# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            duplicate = False
            while current.next and current.val == current.next.val:
                duplicate = True
                current = current.next

            if duplicate:
                prev.next = current.next
            else:
                prev = prev.next

            current = current.next

        return dummy.next