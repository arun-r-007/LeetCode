class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next

        return dummy.next