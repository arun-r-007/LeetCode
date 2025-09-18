# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is None and head.val <= 4 :
            head.val = head.val * 2
            return head

        ls = []
        current = head
        while current is not None :
            ls.append(current.val)
            current = current.next


        n = len(ls)

        singleNumber = int("".join(map(str,ls)))

        head = None

        singleNumber = singleNumber * 2

        ls = []
        ls = [int(d) for d in str(singleNumber)]

        dummy = ListNode(0)
        current = dummy
        for val in ls:
            current.next = ListNode(val)
            current = current.next

        return dummy.next
        