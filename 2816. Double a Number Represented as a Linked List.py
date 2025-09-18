# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def doubleIt(self, head):
        head = self.reverseList(head)

        carry = 0
        curr = head
        prev = None
        while curr:
            val = curr.val * 2 + carry
            curr.val = val % 10
            carry = val // 10
            prev = curr
            curr = curr.next

        if carry:
            prev.next = ListNode(carry)

        return self.reverseList(head)







































# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def doubleIt(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         if head.next is None and head.val <= 4 :
#             head.val = head.val * 2
#             return head

#         ls = []
#         current = head
#         while current is not None :
#             ls.append(current.val)
#             current = current.next


#         n = len(ls)

#         singleNumber = int("".join(map(str,ls)))

#         head = None

#         singleNumber = singleNumber * 2

#         ls = []
#         ls = [int(d) for d in str(singleNumber)]

#         dummy = ListNode(0)
#         current = dummy
#         for val in ls:
#             current.next = ListNode(val)
#             current = current.next

#         return dummy.next
        